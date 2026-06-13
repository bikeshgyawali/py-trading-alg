from src.data import data
from src.strategies import choose_random
from src import config

portfolio = config.load_config()["simulation"]["initial_portfolio"]
shares = config.load_config()["simulation"]["initial_shares"]
ticker = config.load_config()["data"]["ticker"]
start_date = config.load_config()["data"]["start_date"]
end_date = config.load_config()["data"]["end_date"]


def backtest(portfolio, shares, ticker, start_date, end_date):

    curr = data.get_spy_data(ticker, start_date, end_date)

    for eod_close_price in curr:

        eod_close_price, portfolio, shares = choose_random.choose_random(eod_close_price, portfolio, shares)

    total_final_value = portfolio + (shares * eod_close_price)
    return total_final_value


if __name__ == "__main__":
   print(backtest(portfolio, shares, ticker, start_date, end_date))





    