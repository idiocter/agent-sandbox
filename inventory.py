from decimal import Decimal, ROUND_HALF_UP

def apply_discount(price: float, percent: float) -> float:
    """Return `price` reduced by `percent` percent. e.g. 100 at 10% -> 90.0"""
    price_dec = Decimal(str(price))
    percent_dec = Decimal(str(percent))
    discounted = price_dec * (Decimal('100') - percent_dec) / Decimal('100')
    return float(discounted.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

def total_after_discount(prices: list[float], percent: float) -> float:
    """Sum all prices, each with the discount applied. Ignore negative prices."""
    total = Decimal('0')
    percent_dec = Decimal(str(percent))
    for p in prices:
        if p >= 0:
            price_dec = Decimal(str(p))
            discounted = price_dec * (Decimal('100') - percent_dec) / Decimal('100')
            total += discounted
    return float(total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
