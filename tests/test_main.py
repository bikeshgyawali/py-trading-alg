import pytest
import main

def test_backtest_with_static_prices():
    main.settings["strategy"] = "buy and hold"
    
    def dummy_buy_hold(price, portfolio, shares):
        if portfolio >= price:
            return portfolio - price, shares + 1
        return portfolio, shares

    main.available_strategies["buy and hold"] = dummy_buy_hold
    main.data.get_spy_data = lambda ticker, start, end: [100.0, 200.0]

    result = main.backtest(100.0, 0, "SPY", "2015-01-01", "2015-12-31")
    assert result == 200.0

def test_backtest_with_no_prices():
    main.data.get_spy_data = lambda ticker, start, end: []
    
    result = main.backtest(10000.0, 5, "SPY", "2015-01-01", "2015-12-31")
    assert result == 10000.0