"""
prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
max_profit = 30


NOTE: return max difference (X[i]-X[k]) so that X[i] > Y[k]
"""
import math

def max_profit(prices):
    max_profit_value = 0
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[i] < prices[j]:
                difference = prices[j] - prices[i]
                if difference > max_profit_value:
                    max_profit_value = difference
    return max_profit_value


# divide and conquer approach
def max_profit_rec(prices):
    n = len(prices)
    #basecase
    if n <= 1:
        return prices[0], prices[0], 0
    middle = math.ceil(n/2)
    min_l, max_l, max_diff_l = max_profit_rec(prices[0: middle])
    min_r, max_r, max_diff_r = max_profit_rec(prices[middle: n])

    return min([min_l, min_r]), max([max_r, max_l]), max([max_diff_l, max_diff_r, (max_r - min_l)])


def wrapper_mp_rec(prices):
    return max_profit_rec(prices)[2]

# book solution

def max_profit_book(prices):
    min_price_so_far, max_profit = float("inf"), 0.0
    for price in prices:
        max_profit_today = price - min_price_so_far
        max_profit = max(max_profit_today, max_profit)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit



prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
max_profit_ = 30

print(max_profit_book(prices))
