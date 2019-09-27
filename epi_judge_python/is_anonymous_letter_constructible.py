from collections import Counter

from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # Subtraction of counter only retains keys with positive counts
    return not Counter(letter_text) - Counter(magazine_text)

    # char_count = Counter(letter_text)
    # for c in magazine_text:
    #     if c in char_count:
    #         char_count[c] -= 1
    #     if char_count[c] == 0:
    #         del char_count[c]
    #         if not char_count:
    #             return True
    #
    # return not char_count


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
