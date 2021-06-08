'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers
p13.txt
'''

with open('p13.txt', 'r') as i:
    inp = []
    for line in i:
        inp.append(int(line))

def sum_list_of_nums(l):
    sum = 0
    for num in l:
        sum += num
    return sum


if __name__ == "__main__":
    print(str(sum_list_of_nums(inp))[:10])
