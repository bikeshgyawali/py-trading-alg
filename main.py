from src.data import data
from src.strategies import choose_random
from src.strategies import buy_hold
from src.strategies import short_SMA_cross
from src.strategies import long_SMA_cross

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
    "long term SMA crossover" : long_SMA_cross.long_SMA_cross

}


def backtest(portfolio, shares, ticker, start_date, end_date):

    curr = data.get_spy_data(ticker, start_date, end_date)

    last_price = 0.0
    current_history = []
    for price in curr:

        portfolio, shares, current_history = available_strategies[settings["strategy"]](price, portfolio, shares, current_history)
        last_price = price

    total_final_value = portfolio + (shares * last_price)
    return total_final_value


if __name__ == "__main__":
   print(backtest(portfolio, shares, ticker, start_date, end_date))





    