#! /usr/bin/env python

import math
import decimal


decimal.getcontext().prec = (
    102  # Calculate to higher precision to prevent rounding errors
)


def p80():
    total_sum = 0
    for i in range(1, 100):
        if int(math.sqrt(i)) == math.sqrt(i):
            continue
        else:
            sqrt_digits = decimal.Decimal(i).sqrt() * 10 ** 99  # Multiply by 10^99
            # total_sum += sum(map(int, list(str(sqrt_digits)[2:-5])))
            total_sum += sum(sqrt_digits.as_tuple()[1][:100])
    return total_sum


if __name__ == "__main__":
    print(p80())
