import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree, node0, node1):
    def lca_helper(tree, node0, node1):
        if not tree:
            return (0, None)

        left_result = lca_helper(tree.left, node0, node1)
        if left_result[0] == 2:
            return left_result

        right_result = lca_helper(tree.right, node0, node1)
        if right_result[0] == 2:
            return right_result

        count = left_result[0] + right_result[0]
        if tree is node0:
            count += 1
        if tree is node1:
            count += 1

        if count == 2:
            return (count, tree)
        else:
            return (count, None)

    return lca_helper(tree, node0, node1)[1]


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
