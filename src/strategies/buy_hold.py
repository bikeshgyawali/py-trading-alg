from src.utils.friction import buy_friction, sell_friction

def buy_hold(eod_close_price,portfolio,shares):
    
    total_cost = buy_friction(eod_close_price)
    if portfolio >= total_cost:

        total_shares = portfolio // eod_close_price
        portfolio -= buy_friction(eod_close_price * total_shares)
        shares = total_shares

    return portfolio, shares