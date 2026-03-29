"""Price resolution service."""
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from heapq import heappop, heappush

from app.models.price import Price
from app.repositories.price_repo import PriceRepo


@dataclass(frozen=True)
class PriceResult:
    value: float
    path: tuple[int, ...]
    used_prices: tuple[Price, ...]


class PriceService:
    def __init__(self, price_repo: PriceRepo):
        self.price_repo = price_repo

    def get_price(
        self,
        of_curr: int,
        in_curr: int,
        date: datetime = datetime.now(),
        max_delta_before: timedelta | None = None,
        max_delta_after: timedelta | None = None,
        sources: list[str] | None = None,
    ) -> PriceResult | None:
        if of_curr == in_curr:
            return PriceResult(value=1.0, path=(of_curr,), used_prices=())

        date = date.astimezone(timezone.utc)
        best_prices = _select_best_prices(
            self.price_repo.get_candidates(
                target_date=date,
                max_delta_before=max_delta_before,
                max_delta_after=max_delta_after,
                sources=sources,
            ),
            date,
        )
        graph = _build_graph(best_prices, date)
        return _find_best_path(graph, of_curr, in_curr)


@dataclass(frozen=True)
class _PriceEdge:
    to_curr: int
    factor: float
    price: Price
    date_distance_seconds: float


@dataclass(frozen=True)
class _PriceState:
    curr: int
    hops: int
    worst_distance_seconds: float
    value: float
    path: tuple[int, ...]
    prices: tuple[Price, ...]


def _select_best_prices(candidates: list[Price], target_dt: datetime) -> list[Price]:
    by_pair: dict[tuple[int, int], Price] = {}
    for price in candidates:
        pair_key = tuple(sorted((price.of_curr, price.in_curr)))
        current = by_pair.get(pair_key)
        if current is None or _price_sort_key(price, target_dt) < _price_sort_key(current, target_dt):
            by_pair[pair_key] = price
    return list(by_pair.values())


def _price_sort_key(price: Price, target_dt: datetime) -> tuple[float, int]:
    distance = abs((price.date - target_dt).total_seconds())
    return (distance, price.id)


def _build_graph(prices: list[Price], target_dt: datetime) -> dict[int, list[_PriceEdge]]:
    graph: dict[int, list[_PriceEdge]] = {}
    for price in prices:
        distance = _price_sort_key(price, target_dt)[0]
        graph.setdefault(price.of_curr, []).append(
            _PriceEdge(to_curr=price.in_curr, factor=price.value, price=price, date_distance_seconds=distance)
        )
        graph.setdefault(price.in_curr, []).append(
            _PriceEdge(to_curr=price.of_curr, factor=1 / price.value, price=price, date_distance_seconds=distance)
        )
    return graph


def _find_best_path(
    graph: dict[int, list[_PriceEdge]],
    start_curr: int,
    end_curr: int,
) -> PriceResult | None:
    queue: list[tuple[int, float, tuple[int, ...], _PriceState]] = []
    initial = _PriceState(
        curr=start_curr,
        hops=0,
        worst_distance_seconds=0.0,
        value=1.0,
        path=(start_curr,),
        prices=(),
    )
    heappush(queue, (0, 0.0, initial.path, initial))
    best_seen: dict[int, tuple[int, float]] = {start_curr: (0, 0.0)}

    while queue:
        _, _, _, state = heappop(queue)
        if state.curr == end_curr:
            return PriceResult(value=state.value, path=state.path, used_prices=state.prices)

        for edge in graph.get(state.curr, []):
            if edge.to_curr in state.path:
                continue

            next_hops = state.hops + 1
            next_worst = max(state.worst_distance_seconds, edge.date_distance_seconds)
            previous_best = best_seen.get(edge.to_curr)
            if previous_best is not None and (next_hops, next_worst) >= previous_best:
                continue

            next_state = _PriceState(
                curr=edge.to_curr,
                hops=next_hops,
                worst_distance_seconds=next_worst,
                value=state.value * edge.factor,
                path=state.path + (edge.to_curr,),
                prices=state.prices + (edge.price,),
            )
            best_seen[edge.to_curr] = (next_hops, next_worst)
            heappush(queue, (next_hops, next_worst, next_state.path, next_state))

    return None
