import data
import random



def backtest():


    portfolio = 10000
    shares = 0

    curr = data.get_spy_data()

    for eod_close_price in curr:

        move_decision = random.randint(-1,1)
        match move_decision:
            case -1:
                if shares > 0:
                    shares -= 1
                    portfolio += eod_close_price

            case 1:
                if portfolio > eod_close_price:
                    shares += 1
                    portfolio -= eod_close_price

    total_final_value = portfolio + (shares * eod_close_price)
    return total_final_value


if __name__ == "__main__":
   print(backtest())




    