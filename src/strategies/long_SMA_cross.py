from src.utils.friction import buy_friction, sell_friction

def long_SMA_cross(eod_close_price,portfolio,shares, history=None):
    
    if history is None : 
        history = []
    history.append(eod_close_price)

    curr_50_ma = 0.0
    curr_200_ma = 0.0

    if len(history) < 50 :
        curr_50_ma = sum(history) / len(history)
    else:
        curr_50_ma = sum(history[-50:]) / 50

    if len(history) < 200 :
        curr_200_ma = sum(history) / len(history)
    else:
        curr_200_ma = sum(history[-200:]) / 200

    

    if shares > 0 and curr_50_ma < curr_200_ma:
        shares -= 1
        portfolio += sell_friction(eod_close_price)

    elif curr_50_ma > curr_200_ma:
        total_cost = buy_friction(eod_close_price)
        if portfolio >= total_cost:
            shares += 1
            portfolio -= total_cost

    return portfolio, shares, history