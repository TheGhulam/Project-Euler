#! /usr/bin/env python


s = 0
for i in range(1, 1001):
    s += i ** i

print(s)
print(str(s)[-10:])
