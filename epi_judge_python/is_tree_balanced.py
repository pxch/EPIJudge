from test_framework import generic_test


def is_balanced_binary_tree(tree):
    def check_balance_and_height(tree):
        if tree is None:
            return True, -1

        l_balance, l_height = check_balance_and_height(tree.left)
        if not l_balance:
            return False, 0

        r_balance, r_height = check_balance_and_height(tree.right)
        if not r_balance:
            return False, 0

        balance = abs(l_height - r_height) <= 1
        height = max(l_height, r_height) + 1

        return balance, height

    return check_balance_and_height(tree)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
