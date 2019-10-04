from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L, start, finish):
    # More explicitly swapping the next fields
    # if not L:
    #     return None
    #
    # if start < 1 or finish < 1:
    #     return L
    #
    # curr, prev = L, None
    # while start > 1:
    #     prev, curr = curr, curr.next
    #     start, finish = start - 1, finish - 1
    #
    # sublist_tail, sublist_head = curr, prev
    # while finish:
    #     third = curr.next
    #     curr.next = prev
    #     prev, curr = curr, third
    #     finish -= 1
    #
    # if sublist_head:
    #     sublist_head.next = prev
    # else:
    #     L = prev
    # sublist_tail.next = curr
    #
    # return L

    dummy_head = sublist_head = ListNode(0, L)

    for _ in range(start - 1):
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = temp.next, sublist_head.next, temp

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
