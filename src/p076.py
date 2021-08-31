#! /usr/bin/env python


def p76():
    target = 100
    ways = [0 for _ in range(target + 1)]
    ways[0] = 1

    for i in range(1, target):
        for j in range(i, target + 1):
            ways[j] += ways[j - i]
    print(ways[-1])


def count_number_of_ways_to_sum(target_sum):
    """
    Compute the number of unique ways (order does not matter) of summing to target_sum
    using numbers from 1 to target_sum, exclusive.
    """
    if target_sum <= 1:
        raise ValueError("there are no numbers greater than 0 less than the target sum")

    # ith index contains the answer to the (i + 1)th subproblem
    num_ways_to_sum = [0] * (target_sum + 1)

    # There is only 1 way to sum to 1
    num_ways_to_sum[0] = 1

    # Consider sums involving numbers in [1, target_sum)
    for i in range(1, target_sum):
        # Every subproblem j >= i depends on i
        for j in range(i, target_sum + 1):
            # The number of ways to sum j includes all the ways to sum i
            # with all the ways to sum (j - i) appended (like the parenthesis)
            num_ways_to_sum[j] += num_ways_to_sum[j - i]

    return num_ways_to_sum[target_sum]


if __name__ == "__main__":
    p76()
