from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    neg = False
    if x < 0:
        x, neg = -x, True

    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x = x // 10
        if x == 0:
            break

    return ('-' if neg else '') + ''.join(reversed(s))


def string_to_int(s):
    neg = False
    if s.startswith('-'):
        s, neg = s[1:], True

    x = 0
    for c in s:
        x *= 10
        x += ord(c) - ord('0')

    return -x if neg else x


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
