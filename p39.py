from collections import Counter

# p = a + b + math.sqrt(a**2 + b**2)
# Now if we consider b = 0
# p = 2a
# so 2a <= 1000 and a <= 500

def main():
    perimeters = []
    for a in range(500):
        for b in range(500):
            c = (a**2 + b**2)**0.5
            if int(c) == c and ((a + b + c) <= 1000):
                perimeters.append(a+b+c)
    p = Counter(perimeters)
    # Print "1" most common perimeter along with its occurence
    return p.most_common(1)[0]

print(main())




