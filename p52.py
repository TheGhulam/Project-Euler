#! /usr/bin/env python


def sameDigits(a, b):
    return sorted(str(a)) == sorted(str(b))


def main():
    found = False
    i = 2
    while not found:
        x2 = i * 2
        x3 = i * 3
        x4 = i * 4
        x5 = i * 5
        x6 = i * 6
        if (
            sameDigits(i, x2)
            and sameDigits(i, x3)
            and sameDigits(i, x4)
            and sameDigits(i, x5)
            and sameDigits(i, x6)
        ):
            found = True
            print(i)
        i += 1


if __name__ == "__main__":
    main()
