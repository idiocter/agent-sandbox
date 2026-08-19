from inventory import apply_discount, total_after_discount


def test_apply_discount_uses_percentage_not_flat_amount():
    assert apply_discount(100.0, 10.0) == 90.0


def test_apply_discount_zero_percent_is_unchanged():
    assert apply_discount(50.0, 0.0) == 50.0


def test_total_after_discount():
    assert total_after_discount([100.0, 200.0], 10.0) == 270.0
