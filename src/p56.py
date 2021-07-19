#! /usr/bin/env python


def digital_sum(n):
    return sum([int(i) for i in str(n)])


def main():
    m = 0
    for a in range(1, 101):
        for b in range(1, 101):
            s = digital_sum(a ** b)
            if s > m:
                m = s
    return m


if __name__ == "__main__":
    print(main())
