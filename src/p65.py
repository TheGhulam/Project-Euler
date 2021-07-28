#! /usr/bin/env python


def nth_conv_num_of_e(convergent):
    """Returns the numerator of nth convergent of the continued fraction for e

    >>> nth_conv_num_of_e(10)
    1457
    """
    n = 2
    d = 1

    for i in range(2, convergent + 1):
        # n_k = a_k * n_k-1 + n_k-2
        # n   = c   * d     + temp
        temp = d
        c = 2 * (i // 3) if (i % 3 == 0) else 1  # [0,1,1,2,1,1,4,1,1,6,1...]
        d = n
        n = c * d + temp
    return n


if __name__ == "__main__":
    print(sum(map(int, str(nth_conv_num_of_e(100)))))
