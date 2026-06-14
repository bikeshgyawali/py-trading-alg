from src.utils.friction import buy_friction, sell_friction

def short_SMA_cross(eod_close_price,portfolio,shares, history=None):
    
    if history is None : 
        history = []
    history.append(eod_close_price)

    curr_5_ma = 0.0
    curr_20_ma = 0.0

    if len(history) < 5 :
        curr_5_ma = sum(history) / len(history)
    else:
        curr_5_ma = sum(history[-5:]) / 5

    if len(history) < 20 :
        curr_20_ma = sum(history) / len(history)
    else:
        curr_20_ma = sum(history[-20:]) / 20

    

    if shares > 0 and curr_5_ma < curr_20_ma:
        shares -= 1
        portfolio += sell_friction(eod_close_price)

    elif curr_5_ma > curr_20_ma:
        total_cost = buy_friction(eod_close_price)
        if portfolio >= total_cost:
            shares += 1
            portfolio -= total_cost

    return portfolio, shares, history