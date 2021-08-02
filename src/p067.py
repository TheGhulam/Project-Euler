#! /usr/bin/env python


with open("../data/p067_triangle.txt", "r") as f:
    pyramid = []
    for line in f:
        line = line.strip().split(" ")
        pyramid.append(list(map(int, line)))


# # Test pyramid
# test_input = '''3
# 7 4
# 2 4 6
# 8 5 9 3'''
#
# test_pyramid = []
# for l in test_input.split('\n'):
#     test_pyramid.append(list(map(int, l.strip().split(' '))))


def max_path_in_pyramid(p):
    for i in range(len(p) - 2, -1, -1):  # Length of pyramid-2 to 0 reversed
        for j in range(len(p[i])):
            p[i][j] += max(p[i + 1][j], p[i + 1][j + 1])
    p.pop()
    return p


def main():
    print(max_path_in_pyramid(pyramid)[0][0])


if __name__ == "__main__":
    main()
