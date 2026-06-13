import data
from strategies import choose_random



def backtest():


    portfolio = 10000
    shares = 0

    curr = data.get_spy_data()

    for eod_close_price in curr:

        eod_close_price, portfolio, shares = choose_random.choose_random(eod_close_price, portfolio, shares)

    total_final_value = portfolio + (shares * eod_close_price)
    return total_final_value


if __name__ == "__main__":
   print(backtest())




    