from itertools import permutations

def lexicographical_permutation(s):
    perm = sorted(''.join(chars) for chars in permutations(s))
    return perm

print(lexicographical_permutation('0123456789')[1_000_000-1])
