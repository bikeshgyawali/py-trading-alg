import random

def choose_random(eod_close_price,portfolio,shares):
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

        return eod_close_price,portfolio,shares