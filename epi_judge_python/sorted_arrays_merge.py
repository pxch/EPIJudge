import heapq

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays):
    # heapq module has a merge method that can do the job in one line
    # return list(heapq.merge(*sorted_arrays))

    min_heap = []
    sorted_arrays_iters = [iter(sorted_array) for sorted_array in sorted_arrays]

    for i, it in enumerate(sorted_arrays_iters):
        elem = next(it, None)
        if elem is not None:
            heapq.heappush(min_heap, (elem, i))

    res = []
    while min_heap:
        elem, i = heapq.heappop(min_heap)
        res.append(elem)
        next_elem = next(sorted_arrays_iters[i], None)
        if next_elem is not None:
            heapq.heappush(min_heap, (next_elem, i))

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
