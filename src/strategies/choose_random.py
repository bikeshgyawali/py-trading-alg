import random
from src.utils.friction import buy_friction, sell_friction

def choose_random(eod_close_price,portfolio,shares):
        move_decision = random.randint(-1,1)
        match move_decision:
            case -1:
                if shares > 0:
                    shares -= 1
                    portfolio += sell_friction(eod_close_price)

            case 1:
                total_cost = buy_friction(eod_close_price)
                if portfolio >= total_cost:
                    shares += 1
                    portfolio -= total_cost

        return portfolio,shares