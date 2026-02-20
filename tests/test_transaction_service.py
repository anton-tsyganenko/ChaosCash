"""Tests for the transaction service."""
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
from app.services.transaction_service import TransactionService


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
    }


@pytest.fixture
def service(repos):
    return TransactionService(repos["trans"], repos["split"])


def test_create_transaction(service, repos):
    trans_id = service.create_transaction("Test transaction")
    trans = repos["trans"].get_by_id(trans_id)
    assert trans is not None
    assert trans.description == "Test transaction"


def test_delete_transaction_cascades(service, repos):
    cur_id = repos["currency"].insert("USD", "CURR", None, 100)
    acc_id = repos["account"].insert(None, "Cash", None, None, None, "ACT")
    trans_id = service.create_transaction("Test")
    service.add_split(trans_id, acc_id, cur_id, amount=1000)
    service.delete_transaction(trans_id)
    # Splits should be gone via CASCADE
    splits = repos["split"].get_by_transaction(trans_id)
    assert splits == []


def test_duplicate_transaction(service, repos):
    cur_id = repos["currency"].insert("USD", "CURR", None, 100)
    acc_id = repos["account"].insert(None, "Cash", None, None, None, "ACT")
    acc2_id = repos["account"].insert(None, "Bank", None, None, None, "ACT")
    trans_id = service.create_transaction("Original")
    service.add_split(trans_id, acc_id, cur_id, amount=1000)
    service.add_split(trans_id, acc2_id, cur_id, amount=-1000)

    new_id = service.duplicate_transaction(trans_id)
    assert new_id != trans_id

    orig_splits = repos["split"].get_by_transaction(trans_id)
    new_splits = repos["split"].get_by_transaction(new_id)
    assert len(orig_splits) == len(new_splits)
    assert new_splits[0].amount == orig_splits[0].amount


def test_reverse_transaction(service, repos):
    cur_id = repos["currency"].insert("USD", "CURR", None, 100)
    acc_id = repos["account"].insert(None, "Cash", None, None, None, "ACT")
    acc2_id = repos["account"].insert(None, "Bank", None, None, None, "ACT")
    trans_id = service.create_transaction("Payment")
    service.add_split(trans_id, acc_id, cur_id, amount=5000)
    service.add_split(trans_id, acc2_id, cur_id, amount=-5000)

    rev_id = service.reverse_transaction(trans_id)
    rev_trans = repos["trans"].get_by_id(rev_id)
    assert "Reversal" in rev_trans.description

    rev_splits = repos["split"].get_by_transaction(rev_id)
    amounts = sorted(s.amount for s in rev_splits)
    assert amounts == [-5000, 5000]


def test_update_split_fixed(service, repos):
    cur_id = repos["currency"].insert("USD", "CURR", None, 100)
    acc_id = repos["account"].insert(None, "Cash", None, None, None, "ACT")
    trans_id = service.create_transaction("Test")
    split_id = service.add_split(trans_id, acc_id, cur_id, amount=1000, amount_fixed=False)

    split = repos["split"].get_by_id(split_id)
    assert split.amount_fixed is False

    service.update_split_fixed(split_id, True)
    split = repos["split"].get_by_id(split_id)
    assert split.amount_fixed is True

    service.update_split_fixed(split_id, False)
    split = repos["split"].get_by_id(split_id)
    assert split.amount_fixed is False


def test_recalculate_flexible_splits(service, repos):
    cur_id = repos["currency"].insert("USD", "CURR", None, 100)
    acc1 = repos["account"].insert(None, "A", None, None, None, "ACT")
    acc2 = repos["account"].insert(None, "B", None, None, None, "ACT")
    acc3 = repos["account"].insert(None, "C", None, None, None, "ACT")

    trans_id = service.create_transaction("Test")
    s1 = service.add_split(trans_id, acc1, cur_id, amount=10000, amount_fixed=True)
    s2 = service.add_split(trans_id, acc2, cur_id, amount=-5000, amount_fixed=False)
    s3 = service.add_split(trans_id, acc3, cur_id, amount=-5000, amount_fixed=False)

    # Change s1 to 12000, flexible splits should adjust to maintain balance
    result = service.recalculate_flexible_splits(s1, 12000, cur_id, trans_id)
    assert result  # recalculation happened

    updated_splits = repos["split"].get_by_transaction(trans_id)
    total = sum(s.amount for s in updated_splits if s.id != s1)
    # After recalc, total of flexible + fixed should be 0
    # s1 is now 12000, flexible should sum to -12000
    assert total == -12000
