import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):
    # brute-force, with O(n) time and O(n) extra space, best in time
    # pivot = A[pivot_index]
    # left, middle, right = [], [], []
    #
    # for x in A:
    #     if x < pivot:
    #         left.append(x)
    #     elif x > pivot:
    #         right.append(x)
    #     else:
    #         middle.append(x)
    #
    # A[:] = left + middle + right

    # in-place with 2 passes, O(1) space
    # pivot = A[pivot_index]
    #
    # smaller = 0
    # for i in range(len(A)):
    #     if A[i] < pivot:
    #         A[i], A[smaller] = A[smaller], A[i]
    #         smaller += 1
    #
    # larger = len(A) - 1
    # for i in reversed(range(len(A))):
    #     if A[i] > pivot:
    #         A[i], A[larger] = A[larger], A[i]
    #         larger -= 1

    # better solution with only 1 pass, still O(1) space
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)

    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
