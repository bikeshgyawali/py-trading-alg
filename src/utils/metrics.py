import math
import statistics


def daily_returns(values):
    if len(values) < 2:
        return []

    returns = []
    for previous, current in zip(values, values[1:]):
        if previous == 0:
            returns.append(0.0)
        else:
            returns.append((current / previous) - 1)
    return returns


def average_daily_return(values):
    returns = daily_returns(values)
    if not returns:
        return 0.0
    return statistics.mean(returns)


def max_drawdown(values):
    if not values:
        return 0.0

    peak = values[0]
    max_dd = 0.0
    for value in values:
        if value > peak:
            peak = value
        elif peak > 0:
            drawdown = (peak - value) / peak
            if drawdown > max_dd:
                max_dd = drawdown
    return max_dd


def sharpe_ratio(returns, trading_days=252):
    if len(returns) < 2:
        return 0.0

    mean_return = statistics.mean(returns)
    stdev = statistics.pstdev(returns)
    if stdev == 0.0:
        return 0.0

    return (mean_return / stdev) * math.sqrt(trading_days)


def compute_metrics(portfolio_values, market_prices):
    strategy_returns = daily_returns(portfolio_values)
    market_returns = daily_returns(market_prices)

    return {
        "average_daily_portfolio_return": average_daily_return(portfolio_values),
        "alpha_vs_market": statistics.mean(strategy_returns) - statistics.mean(market_returns) if strategy_returns and market_returns else 0.0,
        "maximum_drawdown": max_drawdown(portfolio_values),
        "sharpe_ratio": sharpe_ratio(strategy_returns),
    }
