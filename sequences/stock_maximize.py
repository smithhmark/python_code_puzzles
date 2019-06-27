


def max_profit(prices):
    return 0

def clever(prices, get_trades=False):
    mx_to_come = prices[-1]
    mx_at = len(prices)-1
    profit = 0
    trades = []
    for ii in range(len(prices)-2, -1, -1):
        current = prices[ii]
        if mx_to_come > current:
            trade = ii, mx_at
            trades.append(trade)
            profit += mx_to_come - current
        else:
            mx_to_come = current
            mx_at = ii

    if get_trades:
        return profit, trades
    else:
        return profit

def brute(prices):
    tot = 0
    for ii, pp in enumerate(prices[:-1]):
        profit = 0
        for sp in prices[ii+1:]:
            potential = sp - pp
            if potential > profit:
                profit = potential 
                #print("profit:",sp - pp) 
        tot += profit
    return tot
