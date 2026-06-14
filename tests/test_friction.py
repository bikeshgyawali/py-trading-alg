import pytest
from src.utils.friction import buy_friction, sell_friction

def test_buy_friction_increases_price():
    result = buy_friction(100.0)
    assert result == 100.01

def test_sell_friction_decreases_price():
    result = sell_friction(100.0)
    assert result == 99.99

def test_buy_friction_zero_price():
    result = buy_friction(0.0)
    assert result == 0.0

def test_sell_friction_zero_price():
    result = sell_friction(0.0)
    assert result == 0.0