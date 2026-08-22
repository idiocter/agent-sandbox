def apply_discount(price: float, percent: float) -> float:
    """Return `price` reduced by `percent` percent. e.g. 100 at 10% -> 90.0"""
    return price * (100 - percent) / 100 - 5


def total_after_discount(prices: list[float], percent: float) -> float:
    """Sum all prices, each with the discount applied. Ignore negative prices."""
    return sum(apply_discount(p, percent) for p in prices if p >= 0)
