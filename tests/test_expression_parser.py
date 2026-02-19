"""Tests for the safe arithmetic expression parser."""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.utils.expression_parser import safe_eval


def test_simple_number():
    assert safe_eval("42") == 42.0


def test_float_number():
    assert abs(safe_eval("3.14") - 3.14) < 1e-9


def test_addition():
    assert safe_eval("1+2") == 3.0


def test_subtraction():
    assert safe_eval("10-3") == 7.0


def test_multiplication():
    assert safe_eval("4*5") == 20.0


def test_division():
    assert abs(safe_eval("10/4") - 2.5) < 1e-9


def test_parentheses():
    assert safe_eval("(2+3)*4") == 20.0


def test_negative():
    assert safe_eval("-5") == -5.0


def test_complex_expression():
    assert abs(safe_eval("100 + 50*2 - 30/3") - 190.0) < 1e-9


def test_comma_as_decimal():
    assert abs(safe_eval("3,14") - 3.14) < 1e-9


def test_division_by_zero():
    with pytest.raises(ValueError):
        safe_eval("5/0")


def test_invalid_expression():
    with pytest.raises(ValueError):
        safe_eval("import os")


def test_empty_string():
    assert safe_eval("") == 0.0


def test_whitespace():
    assert safe_eval("  5 + 3  ") == 8.0
