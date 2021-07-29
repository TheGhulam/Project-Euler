#! /usr/bin/env python
from itertools import permutations
from itertools import groupby

with open("p059_cipher.txt", "r") as f:
    data = f.readline().strip().split(",")
    data = list(map(int, data))


def encrypt(l, k):
    """encrypt/decrypt
    Takes a list of ascii codes and returns XORed version of codes in original form
    """
    data = []
    for i in range(len(l)):
        data.append(chr(l[i] ^ int(k[i % len(k)])))
    return data


## Task: Frequency analysis to check most common codes against common alphabets
nums = [list(group)[0] for key, group in groupby(sorted(data))]
freq = [len(list(group)) for key, group in groupby(sorted(data))]
# print(list(zip(nums, freq)))

# Found these possible chars after trial and error
# Possiblechars = ['p', 'x', 'v', 'r', 'x', 'b', 'a', 'e', 'i', 'o', 'u']


## Task: Further analysis of Possiblechars to see which chars produce the lowest foreign chars

# for char in Possiblechars:
#     print(char)
#     for n in data:
#         print(chr(n ^ ord(char)), end="")
#     print('\n')

# Narrowed down chars to "epx". Now need to check the order of chars in key


## Task: Determine the order of chars in key

# key = [ord('e'), ord('p'), ord('x')]
# for perm in permutations(key, 3):
#     print(list(map(chr, perm)))
#     print("".join(encrypt(data, list(perm))))
#     print('\n')

# Manually checked all outputs to confirm key: 'exp'


## Task: Find sum of ASCII values
decrypted_text = "".join(encrypt(data, [ord("e"), ord("x"), ord("p")]))

s = 0
for char in list(decrypted_text):
    s += ord(char)
print(s)
