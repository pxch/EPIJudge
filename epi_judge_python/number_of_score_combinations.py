from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):
    dp = [[1] + [0] * final_score for _ in individual_play_scores]

    for i, score in enumerate(individual_play_scores):
        for j in range(1, final_score + 1):
            dp[i][j] = dp[i][j - score] if j >= score else 0
            if i > 0:
                dp[i][j] += dp[i - 1][j]

    return dp[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
