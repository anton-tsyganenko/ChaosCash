"""Tests for the balance service."""
import os
import sqlite3
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.database.schema import ensure_schema
from app.repositories.account_repo import AccountRepo
from app.repositories.currency_repo import CurrencyRepo
from app.repositories.split_repo import SplitRepo
from app.repositories.transaction_repo import TransactionRepo
from app.services.balance_service import BalanceService


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
def balance_service(repos):
    return BalanceService(repos["account"])


def test_empty_account_balance(repos, balance_service):
    acc_id = repos["account"].insert(None, "Cash", None, None, None, False)
    balance = balance_service.get_balance(acc_id)
    assert balance == {}


def test_single_currency_balance(repos, balance_service):
    cur_id = repos["currency"].insert("USD", "CURR", "US Dollar", 100)
    acc_id = repos["account"].insert(None, "Cash", None, None, None, False)
    trans_id = repos["trans"].insert("2024-01-01 00:00:00", "Test")
    repos["split"].insert(trans_id, acc_id, cur_id, None, None, 10000)  # 100.00 USD

    balance = balance_service.get_balance(acc_id)
    assert balance[cur_id] == 10000


def test_multi_currency_balance(repos, balance_service):
    usd_id = repos["currency"].insert("USD", "CURR", "US Dollar", 100)
    eur_id = repos["currency"].insert("EUR", "CURR", "Euro", 100)
    acc_id = repos["account"].insert(None, "Cash", None, None, None, False)
    trans_id = repos["trans"].insert("2024-01-01 00:00:00", "Test")
    repos["split"].insert(trans_id, acc_id, usd_id, None, None, 5000)
    repos["split"].insert(trans_id, acc_id, eur_id, None, None, 3000)

    balance = balance_service.get_balance(acc_id)
    assert balance[usd_id] == 5000
    assert balance[eur_id] == 3000


def test_grp_account_balance(repos, balance_service):
    cur_id = repos["currency"].insert("USD", "CURR", "US Dollar", 100)
    parent_id = repos["account"].insert(None, "Assets", None, None, None, False)
    child1_id = repos["account"].insert(parent_id, "Cash", None, None, None, False)
    child2_id = repos["account"].insert(parent_id, "Bank", None, None, None, False)

    trans_id = repos["trans"].insert("2024-01-01 00:00:00", "Test")
    repos["split"].insert(trans_id, child1_id, cur_id, None, None, 10000)
    repos["split"].insert(trans_id, child2_id, cur_id, None, None, 20000)

    balance = balance_service.get_balance(parent_id)
    assert balance[cur_id] == 30000


def test_cache_invalidation(repos, balance_service):
    cur_id = repos["currency"].insert("USD", "CURR", "US Dollar", 100)
    acc_id = repos["account"].insert(None, "Cash", None, None, None, False)
    trans_id = repos["trans"].insert("2024-01-01 00:00:00", "Test")
    split_id = repos["split"].insert(trans_id, acc_id, cur_id, None, None, 10000)

    # Initial balance
    balance1 = balance_service.get_balance(acc_id)
    assert balance1[cur_id] == 10000

    # Update split amount
    repos["split"].update_amount(split_id, 20000)

    # Invalidate and re-fetch
    balance_service.invalidate(acc_id, cur_id)
    balance2 = balance_service.get_balance(acc_id)
    assert balance2[cur_id] == 20000
