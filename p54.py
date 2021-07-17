#! /usr/bin/env python
import itertools


def eval_hand(hand):
    """
    # Return ranking followed by tie-break information.
    # 8. Straight Flush
    # 7. Four of a Kind
    # 6. Full House
    # 5. Flush
    # 4. Straight
    # 3. Three of a Kind
    # 2. Two pair
    # 1. One pair
    # 0. High card

    >>> eval_hand([(8, 'C'), (10, 'S'), (13, 'C'), (9, 'H'), (4, 'S')])
    (0, [], [13, 10, 9, 8, 7, 4])
    """

    values = sorted([c[0] for c in hand], reverse=True)
    suits = [c[1] for c in hand]
    straight = values == list(range(values[0], values[0] - 5, -1)) or values == [
        14,
        5,
        4,
        3,
        2,
    ]
    flush = all(s == suits[0] for s in suits)

    if straight and flush:
        return 8, values[1]
    if flush:
        return 5, values
    if straight:
        return 4, values[1]

    trips = []
    pairs = []
    for v, group in itertools.groupby(values):
        count = sum(1 for _ in group)
        if count == 4:
            return 7, v, values
        elif count == 3:
            trips.append(v)
        elif count == 2:
            pairs.append(v)

    if trips:
        return (6 if pairs else 3), trips, pairs, values
    return len(pairs), pairs, values


def main():
    value_dict = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    value_dict.update((str(x), x) for x in range(2, 10))

    player1_wins = 0
    with open("p054_poker.txt") as f:
        for line in f:
            cards = [(value_dict[x[0]], x[1]) for x in line.split(" ")]
            player1_wins += eval_hand(cards[:5]) > eval_hand(cards[5:])

    # print(player2_wins)


if __name__ == "__main__":
    main()
