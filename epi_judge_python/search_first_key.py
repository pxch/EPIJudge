import bisect

from test_framework import generic_test


def search_first_of_k(A, k):
    # the bisect module has a bisect_left method which will just do the trick
    # i = bisect.bisect_left(A, k)
    # return i if 0 <= i < len(A) and A[i] == k else -1

    res = -1
    lo = 0
    hi = len(A) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if A[mid] > k:
            hi = mid - 1
        elif A[mid] == k:
            res = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
