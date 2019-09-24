from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # dp-ish solution, O(n) time and O(1) space
    res = 0.0
    lowest = prices[0]

    for p in prices[1:]:
        res = max(res, p - lowest)
        lowest = min(lowest, p)

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
