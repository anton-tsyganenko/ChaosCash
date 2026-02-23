"""Tests for the integrity service."""
import pytest
import sqlite3
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.database.schema import ensure_schema
from app.repositories.account_repo import AccountRepo
from app.repositories.split_repo import SplitRepo
from app.repositories.currency_repo import CurrencyRepo
from app.repositories.transaction_repo import TransactionRepo
from app.services.integrity_service import IntegrityService


@pytest.fixture
def db():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    ensure_schema(conn)
    return conn


@pytest.fixture
def repos(db):
    return {
        "account": AccountRepo(db),
        "split": SplitRepo(db),
        "currency": CurrencyRepo(db),
        "trans": TransactionRepo(db),
        "conn": db,
    }


@pytest.fixture
def integrity(repos):
    return IntegrityService(repos["trans"], repos["split"], repos["conn"])


def test_no_imbalance_initially(integrity):
    assert not integrity.has_imbalance()


def test_detects_imbalance(repos, integrity):
    cur_id = repos["currency"].insert("USD", "CURR", None, 100)
    acc_id = repos["account"].insert(None, "Cash", None, None, None, False)
    trans_id = repos["trans"].insert("2024-01-01 00:00:00", "Test")
    repos["split"].insert(trans_id, acc_id, cur_id, None, None, 5000)  # unbalanced!
    assert integrity.has_imbalance()


def test_balanced_no_imbalance(repos, integrity):
    cur_id = repos["currency"].insert("USD", "CURR", None, 100)
    acc1 = repos["account"].insert(None, "Cash", None, None, None, False)
    acc2 = repos["account"].insert(None, "Income", None, None, None, False)
    trans_id = repos["trans"].insert("2024-01-01 00:00:00", "Test")
    repos["split"].insert(trans_id, acc1, cur_id, None, None, 5000)
    repos["split"].insert(trans_id, acc2, cur_id, None, None, -5000)
    assert not integrity.has_imbalance()


def test_detects_empty_transactions(repos, integrity):
    repos["trans"].insert("2024-01-01 00:00:00", "Empty trans")
    assert integrity.has_empty_transactions()


def test_no_empty_transactions_initially(integrity):
    assert not integrity.has_empty_transactions()


def test_zero_split_detection(repos, integrity):
    cur_id = repos["currency"].insert("USD", "CURR", None, 100)
    acc_id = repos["account"].insert(None, "Cash", None, None, None, False)
    trans_id = repos["trans"].insert("2024-01-01 00:00:00", "Test")
    split_id = repos["split"].insert(trans_id, acc_id, cur_id, None, None, 0)
    zero_ids = integrity.get_zero_split_ids()
    assert split_id in zero_ids
