import inspect

from src.data import data
from src.strategies import choose_random
from src.strategies import buy_hold
from src.strategies import short_SMA_cross
from src.strategies import long_SMA_cross
from src.strategies import mean_reversion
from src.utils import metrics

from src import config

settings = config.load_config()

portfolio = settings["simulation"]["initial_portfolio"]
shares = settings["simulation"]["initial_shares"]
ticker = settings["data"]["ticker"]
start_date = settings["data"]["start_date"]
end_date = settings["data"]["end_date"]

available_strategies = {

    "random" : choose_random.choose_random,
    "buy and hold" : buy_hold.buy_hold,
    "short term SMA crossover" : short_SMA_cross.short_SMA_cross,
    "long term SMA crossover" : long_SMA_cross.long_SMA_cross,
    "mean reversion" : mean_reversion.mean_reversion

}


def simulate(portfolio, shares, ticker, start_date, end_date):
    prices = data.get_spy_data(ticker, start_date, end_date)
    current_history = []
    portfolio_values = []

    for price in prices:
        strategy = available_strategies[settings["strategy"]]
        try:
            portfolio, shares, current_history = strategy(price, portfolio, shares, current_history)
        except TypeError:
            portfolio, shares = strategy(price, portfolio, shares)
        portfolio_values.append(portfolio + (shares * price))

    return portfolio_values, prices


def backtest(portfolio, shares, ticker, start_date, end_date):
    portfolio_values, _ = simulate(portfolio, shares, ticker, start_date, end_date)
    return portfolio_values[-1] if portfolio_values else portfolio


if __name__ == "__main__":
    portfolio_values, prices = simulate(portfolio, shares, ticker, start_date, end_date)
    final_value = portfolio_values[-1] if portfolio_values else portfolio
    results = metrics.compute_metrics(portfolio_values, prices)

    print(f"Final portfolio value: ${final_value:.2f}")
    print(f"Average daily portfolio return: {results['average_daily_portfolio_return']:.6f}")
    print(f"Strategy alpha vs market return: {results['alpha_vs_market']:.6f}")
    print(f"Maximum drawdown: {results['maximum_drawdown']:.6f}")
    print(f"Sharpe ratio: {results['sharpe_ratio']:.6f}")





    