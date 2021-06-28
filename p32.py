p = set()

for a in range(1, 100):
    for b in range(1, 9999 // a):
        if ''.join(sorted("%d%d%d" % (a, b, a*b))) == '123456789':
            p.add(a * b)

print(sum(p))
