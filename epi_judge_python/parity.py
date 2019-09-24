from test_framework import generic_test


def parity(x):
    # brute-force. O(n)
    # res = 0
    # while x:
    #     res ^= x & 1
    #     x >>= 1
    # return res

    # refinement using x & (x - 1) to remove the lowest set bit. O(k) (k is the number of set bits)
    # res = 0
    # while x:
    #     res ^= 1
    #     x &= x - 1
    #
    # return res

    # exploiting associativity of XOR. O(log n)
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
