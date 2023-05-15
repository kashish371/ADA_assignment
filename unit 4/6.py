# Implement the coin change problem using a greedy approach in Python.

def coin_change_greedy(coins, amount):
    """
    Approximates the coin change problem using a greedy approach for a canonical coin system.
    Returns the minimum number of coins needed to make up the given amount.
    """
    coins.sort(reverse=True)  # Sort coins in descending order
    num_coins = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            num_coins += 1
    return num_coins