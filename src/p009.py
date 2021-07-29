#for c in range(400, 3, -1):
#    for b in range(399, 2, -1):
#        for a in range(398, 1, -1):
#            if (a**2 + b**2) == c**2:
#                if (a + b + c) == 1000:
#                    print(a*b*c)

#Improvised
import numpy

def check_pythagorean(a, b, c):
    return a**2 + b**2 == c**2

def main():
    for a in range(1, 332): # a can't be > 332 as a + b + c = 1000
        for b in range(a+1, int(numpy.ceil((1000-1)/2-1))): # b can't be greater than half of 1000-a
            c = 1000 - a - b
            if (check_pythagorean(a, b, c)):
                print(a*b*c, f"({a}, {b}, {c})")

if __name__ == "__main__":
    main()

