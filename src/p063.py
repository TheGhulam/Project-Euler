#! /usr/bin/env python


def p63():
    count = 0
    for power in range(50):
        for i in range(1, 100):
            num = i ** power
            if len(str(num)) == power:
                count += 1
    return(count)

if __name__ == "__main__":
    print(p63())

