from test_framework import generic_test


def power(x, y):
    res = 1
    if y < 0:
        x, y = 1 / x, -y

    # brute-force
    # while y:
    #     res *= x
    #     y -= 1
    while y:
        if y & 1:
            res *= x
        x, y = x * x, y >> 1

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
