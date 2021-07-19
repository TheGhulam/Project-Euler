from string import ascii_uppercase

def score(word):
    return sum(ascii_uppercase.index(c) + 1 for c in word)

with open('p22_names.txt') as f:
    # names = sorted(f.read().replace('"', '').split(','), key=str)
    names = f.read().replace('"', '').split(',')
    names[-1] = names[-1].strip('\n')
    names = sorted(names, key=str)

print(sum([i*score(x) for i,x in enumerate(names, 1)]))
# print(names[:5])
# print(names[-5:])
# print(score('AARON'))
# print(score('COLIN'))


