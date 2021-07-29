def palindromic(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False


s = 0
for i in range(1_000_000):
    if palindromic(i) and palindromic(int(bin(i)[2:])):
        s += i

print(s)
