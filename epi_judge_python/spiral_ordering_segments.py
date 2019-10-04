from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    res = []
    n = len(square_matrix)

    for k in range(n // 2):
        res.extend(square_matrix[k][k:-1 - k])
        res.extend([square_matrix[j][-1 - k] for j in range(k, n - k - 1)])
        res.extend(square_matrix[-1 - k][-1 - k:k:-1])
        res.extend([square_matrix[j][k] for j in range(n - k - 1, k, -1)])

    if n % 2 == 1:
        res.append(square_matrix[n // 2][n // 2])

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
