target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0] * target

for c in coins:
    for i in range(c, target + 1):
        ways[i] += ways[i - c]

print("Ways to make change =", ways[target])
