"""Tests for price resolution."""
import os
import sqlite3
import sys
from datetime import datetime, timedelta, timezone

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.database.schema import ensure_schema
from app.repositories.currency_repo import CurrencyRepo
from app.repositories.price_repo import PriceRepo
from app.services.price_service import PriceService


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
        "currency": CurrencyRepo(db),
        "price": PriceRepo(db),
    }


@pytest.fixture
def ccy(repos):
    return {
        "USD": repos["currency"].insert("USD", "CURR", "US Dollar", 100),
        "EUR": repos["currency"].insert("EUR", "CURR", "Euro", 100),
        "GBP": repos["currency"].insert("GBP", "CURR", "British Pound", 100),
        "RUB": repos["currency"].insert("RUB", "CURR", "Russian Ruble", 100),
        "JPY": repos["currency"].insert("JPY", "CURR", "Japanese Yen", 1),
    }


@pytest.fixture
def service(repos):
    return PriceService(repos["price"])


def test_returns_direct_price_for_same_currency(service, ccy):
    result = service.get_price(ccy["USD"], ccy["USD"], datetime(2024, 1, 10), timedelta(days=14), timedelta(days=5))
    assert result is not None
    assert result.value == 1.0
    assert result.path == (ccy["USD"],)


def test_uses_closest_direct_price_within_window(service, repos, ccy):
    repos["price"].insert(ccy["USD"], 0.92, ccy["EUR"], datetime(2024, 1, 1), "ECB")
    repos["price"].insert(ccy["USD"], 0.95, ccy["EUR"], datetime(2024, 1, 9), "ECB")

    result = service.get_price(ccy["USD"], ccy["EUR"], datetime(2024, 1, 10), timedelta(days=14), timedelta(days=5))

    assert result is not None
    assert result.value == pytest.approx(0.95)
    assert result.path == (ccy["USD"], ccy["EUR"])
    assert [price.source for price in result.used_prices] == ["ECB"]


def test_can_use_inverse_direction(service, repos, ccy):
    repos["price"].insert(ccy["USD"], 0.8, ccy["EUR"], datetime(2024, 1, 9), "ECB")

    result = service.get_price(ccy["EUR"], ccy["USD"], datetime(2024, 1, 10), timedelta(days=14), timedelta(days=5))

    assert result is not None
    assert result.value == pytest.approx(1.25)
    assert result.path == (ccy["EUR"], ccy["USD"])


def test_prefers_shortest_path_by_number_of_edges(service, repos, ccy):
    repos["price"].insert(ccy["USD"], 0.91, ccy["EUR"], datetime(2024, 1, 9), "ECB")
    repos["price"].insert(ccy["EUR"], 0.86, ccy["GBP"], datetime(2024, 1, 9), "ECB")
    repos["price"].insert(ccy["USD"], 110.0, ccy["JPY"], datetime(2024, 1, 10), "BOJ")
    repos["price"].insert(ccy["JPY"], 0.006, ccy["GBP"], datetime(2024, 1, 10), "BOJ")
    repos["price"].insert(ccy["USD"], 0.79, ccy["GBP"], datetime(2024, 1, 1), "Archive")

    result = service.get_price(ccy["USD"], ccy["GBP"], datetime(2024, 1, 10), timedelta(days=14), timedelta(days=5))

    assert result is not None
    assert result.value == pytest.approx(0.79)
    assert result.path == (ccy["USD"], ccy["GBP"])


def test_prefers_more_recent_path_when_hops_are_equal(service, repos, ccy):
    repos["price"].insert(ccy["USD"], 0.9, ccy["EUR"], datetime(2024, 1, 9), "ECB")
    repos["price"].insert(ccy["EUR"], 0.85, ccy["GBP"], datetime(2024, 1, 8), "ECB")

    repos["price"].insert(ccy["USD"], 89.0, ccy["RUB"], datetime(2024, 1, 2), "CBR")
    repos["price"].insert(ccy["RUB"], 0.0085, ccy["GBP"], datetime(2024, 1, 2), "CBR")

    result = service.get_price(ccy["USD"], ccy["GBP"], datetime(2024, 1, 10), timedelta(days=14), timedelta(days=5))

    assert result is not None
    assert result.path == (ccy["USD"], ccy["EUR"], ccy["GBP"])
    assert result.value == pytest.approx(0.9 * 0.85)


def test_filters_by_sources(service, repos, ccy):
    repos["price"].insert(ccy["USD"], 0.9, ccy["EUR"], datetime(2024, 1, 9), "ECB")
    repos["price"].insert(ccy["USD"], 0.93, ccy["EUR"], datetime(2024, 1, 10), "Broker")

    result = service.get_price(
        ccy["USD"],
        ccy["EUR"],
        datetime(2024, 1, 10),
        timedelta(days=14),
        timedelta(days=5),
        sources=["ECB"],
    )

    assert result is not None
    assert result.value == pytest.approx(0.9)
    assert [price.source for price in result.used_prices] == ["ECB"]


def test_without_lower_bound_uses_older_prices(service, repos, ccy):
    repos["price"].insert(ccy["USD"], 0.88, ccy["EUR"], datetime(2023, 12, 1), "Manual")

    result = service.get_price(
        ccy["USD"],
        ccy["EUR"],
        datetime(2024, 1, 10),
        None,
        timedelta(days=5),
    )

    assert result is not None
    assert result.value == pytest.approx(0.88)
    assert result.used_prices[0].date == datetime(2023, 12, 1).astimezone(timezone.utc)


def test_cross_rate(service, repos, ccy):
    repos["price"].insert(ccy["USD"], 80, ccy["RUB"], datetime(2023, 12, 1), "CBR")
    repos["price"].insert(ccy["EUR"], 95, ccy["RUB"], datetime(2023, 12, 1), "CBR")

    result = service.get_price(
        ccy["EUR"],
        ccy["USD"],
        datetime(2023, 12, 1),
    )

    assert result.value == pytest.approx(95/80)
    assert result.path == (ccy["EUR"], ccy["RUB"], ccy["USD"])


def test_negative_too_old(service, repos, ccy):
    repos["price"].insert(ccy["USD"], 0.88, ccy["EUR"], datetime(2023, 12, 1), "Manual")

    result = service.get_price(
        ccy["USD"],
        ccy["EUR"],
        datetime(2024, 1, 10),
        timedelta(days=5),
        timedelta(days=0),
    )

    assert result is None


def test_negative_too_new(service, repos, ccy):
    repos["price"].insert(ccy["USD"], 0.88, ccy["EUR"], datetime(2024, 12, 1), "Manual")

    result = service.get_price(
        ccy["USD"],
        ccy["EUR"],
        datetime(2024, 1, 10),
        timedelta(days=5),
        timedelta(days=0),
    )

    assert result is None


def test_nearest_future_rate(service, repos, ccy):
    repos["price"].insert(ccy["USD"], 0.88, ccy["EUR"], datetime(2024, 12, 1), "Manual")
    repos["price"].insert(ccy["USD"], 0.85, ccy["EUR"], datetime(2024, 12, 10), "Manual")

    result = service.get_price(
        ccy["USD"],
        ccy["EUR"],
        datetime(2024, 12, 9),
        timedelta(days=10),
        timedelta(days=5),
    )

    assert result.value == 0.85


def test_negative_bad_source(service, repos, ccy):
    repos["price"].insert(ccy["USD"], 0.88, ccy["EUR"], datetime(2023, 12, 1), "CBR")

    result = service.get_price(
        ccy["USD"],
        ccy["EUR"],
        datetime(2023, 12, 1),
        timedelta(days=5),
        timedelta(days=0),
        sources=["ECB"],
    )

    assert result is None


def test_current_time_rate(service, repos, ccy):
    repos["price"].insert(ccy["USD"], 0.85, ccy["EUR"], datetime(2023, 12, 1), "CBR")
    repos["price"].insert(ccy["USD"], 0.88, ccy["EUR"], datetime(2025, 12, 1), "CBR")
    repos["price"].insert(ccy["USD"], 0.90, ccy["EUR"], datetime(3025, 12, 1), "CBR")

    result = service.get_price(
        ccy["USD"],
        ccy["EUR"],
    )

    assert result.value == 0.88

