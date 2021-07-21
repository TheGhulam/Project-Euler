#! /usr/bin/env python


with open('../data/p059_cipher.txt', 'r') as f:
    codes = f.readline().split(',')


def check_english(a, b):
    xor = a ^ b
    if 32 <= xor <= 90:
        return True
    elif 97 <= xor <= 122:
        return True
    return False

def decrypt(s)
