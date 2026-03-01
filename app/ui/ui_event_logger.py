"""Verbose UI event logging for focus and input troubleshooting."""
from __future__ import annotations

import logging
from typing import Any

from PyQt6.QtCore import QEvent, QObject
from PyQt6.QtGui import QKeyEvent, QMouseEvent
from PyQt6.QtWidgets import QAbstractItemView, QApplication, QWidget

EVENT_LOGGER_NAME = "chaoscash.ui.events"


class UIEventLogger(QObject):
    """Global event filter that logs focus, keyboard and mouse events."""

    def __init__(self, parent: QObject | None = None):
        super().__init__(parent)
        self._logger = logging.getLogger(EVENT_LOGGER_NAME)

    def install(self, app: QApplication) -> None:
        """Attach this logger to application-wide events."""
        app.installEventFilter(self)
        app.focusChanged.connect(self._on_focus_changed)
        self._logger.info("UI event logger installed")

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        et = event.type()
        if et in (QEvent.Type.FocusIn, QEvent.Type.FocusOut):
            self._logger.info("focus-event %s", self._describe_event(watched, event))
        elif et in (QEvent.Type.KeyPress, QEvent.Type.KeyRelease):
            self._logger.debug("key-event %s", self._describe_key_event(watched, event))
        elif et in (QEvent.Type.MouseButtonPress, QEvent.Type.MouseButtonRelease, QEvent.Type.MouseButtonDblClick):
            self._logger.debug("mouse-event %s", self._describe_mouse_event(watched, event))
        elif et in (QEvent.Type.InputMethod, QEvent.Type.ShortcutOverride):
            self._logger.debug("input-event %s", self._describe_event(watched, event))
        return super().eventFilter(watched, event)

    def _on_focus_changed(self, old: QWidget | None, now: QWidget | None) -> None:
        self._logger.info(
            "focus-changed from=%s to=%s",
            self._object_name(old),
            self._object_name(now),
        )

    def _describe_key_event(self, watched: QObject, event: QEvent) -> str:
        key_event = event
        if not isinstance(key_event, QKeyEvent):
            return self._describe_event(watched, event)
        return (
            f"target={self._object_name(watched)} type={event.type().name} "
            f"key={key_event.key()} text={key_event.text()!r} "
            f"mods={int(key_event.modifiers().value)} accepted={event.isAccepted()} "
            f"view={self._view_state(watched)}"
        )

    def _describe_mouse_event(self, watched: QObject, event: QEvent) -> str:
        mouse_event = event
        if not isinstance(mouse_event, QMouseEvent):
            return self._describe_event(watched, event)
        pos = mouse_event.position()
        return (
            f"target={self._object_name(watched)} type={event.type().name} "
            f"button={int(mouse_event.button().value)} buttons={int(mouse_event.buttons().value)} "
            f"x={pos.x():.1f} y={pos.y():.1f} accepted={event.isAccepted()} "
            f"view={self._view_state(watched)}"
        )

    def _describe_event(self, watched: QObject, event: QEvent) -> str:
        return (
            f"target={self._object_name(watched)} type={event.type().name} "
            f"accepted={event.isAccepted()} view={self._view_state(watched)}"
        )

    def _view_state(self, watched: QObject) -> str:
        if isinstance(watched, QAbstractItemView):
            try:
                idx = watched.currentIndex()
                editing = watched.state() == QAbstractItemView.State.EditingState
            except RuntimeError as err:
                return f"{watched.__class__.__name__}(state-unavailable:{err})"
            if idx.isValid():
                return (
                    f"{watched.__class__.__name__}(row={idx.row()}, col={idx.column()}, "
                    f"editing={editing})"
                )
            return f"{watched.__class__.__name__}(no-current-index, editing={editing})"
        parent = watched.parent()
        if isinstance(parent, QAbstractItemView):
            try:
                idx = parent.currentIndex()
                editing = parent.state() == QAbstractItemView.State.EditingState
            except RuntimeError as err:
                return f"editor-of-{parent.__class__.__name__}(state-unavailable:{err})"
            if idx.isValid():
                return (
                    f"editor-of-{parent.__class__.__name__}(row={idx.row()}, col={idx.column()}, "
                    f"editing={editing})"
                )
            return f"editor-of-{parent.__class__.__name__}(no-current-index, editing={editing})"
        return "n/a"

    def _object_name(self, obj: Any) -> str:
        if obj is None:
            return "None"
        name = ""
        if isinstance(obj, QObject):
            name = obj.objectName()
        suffix = f"#{name}" if name else ""
        return f"{obj.__class__.__name__}{suffix}"

