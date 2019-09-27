from test_framework import generic_test


def has_three_sum(A, t):
    def has_two_sum(sorted_list, t):
        i, j = 0, len(sorted_list) - 1
        while i <= j:
            if sorted_list[i] + sorted_list[j] < t:
                i += 1
            elif sorted_list[i] + sorted_list[j] == t:
                return True
            else:
                j -= 1
        return False

    A.sort()
    for i in A:
        if has_two_sum(A, t - i):
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
