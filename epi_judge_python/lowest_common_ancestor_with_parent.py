import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0, node1):
    def get_depth(node):
        depth = 0
        while node:
            node = node.parent
            depth += 1
        return depth

    depth0, depth1 = get_depth(node0), get_depth(node1)
    if depth1 > depth0:
        node0, node1 = node1, node0
        depth_diff = depth1 - depth0
    else:
        depth_diff = depth0 - depth1

    while depth_diff:
        node0 = node0.parent
        depth_diff -= 1

    while node0 is not node1:
        node0, node1 = node0.parent, node1.parent

    return node0

    # My original solution
    # p0_set, p1_set = set(), set()
    #
    # p0, p1 = node0, node1
    # while p0 or p1:
    #     if p0 is p1:
    #         return p0
    #     if p0 in p1_set:
    #         return p0
    #     if p1 in p0_set:
    #         return p1
    #     p0_set.add(p0)
    #     p1_set.add(p1)
    #
    #     p0 = p0.parent if p0 else p0
    #     p1 = p1.parent if p1 else p1
    #
    # return None


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_with_parent.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
