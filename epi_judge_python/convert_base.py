import string

from test_framework import generic_test


def convert_base(num_as_string, b1, b2):
    neg = False
    if num_as_string.startswith('-'):
        num_as_string, neg = num_as_string[1:], True

    num_as_int = 0
    for c in num_as_string:
        num_as_int *= b1
        num_as_int += string.hexdigits.index(c.lower())

    res = []
    while True:
        res.append(string.hexdigits[num_as_int % b2].upper())
        num_as_int = num_as_int // b2
        if num_as_int == 0:
            break

    return ('-' if neg else '') + ''.join(reversed(res))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
