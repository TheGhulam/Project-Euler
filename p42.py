#! /usr/bin/env python

with open('p42_words.txt', 'r') as f:
    words = f.read().replace('"','').split(',')


def WordValue(w):
    s = 0
    for l in list(w):
        s += ord(l) - 64
    return s

def main():
    '''
    A triangular number "n" will satisfy the condition of (8n+1) being a
    perfect square for numbers less than (2^53)-1)
    '''
    c = 0
    for w in words:
        s = WordValue(w)
        if (8*s+1)**0.5 == int((8*s+1)**0.5):
            c += 1
    print(c)



if __name__ == "__main__":
    main()
