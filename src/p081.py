#! /usr/bin/env python

test_input = """
131,673,234,103,18
201,96,342,965,150
630,803,746,422,111
537,699,497,121,956
805,732,524,37,331
"""


test_data = []
for line in test_input.strip().split('\n'):
    nums = line.split(',')
    test_data.append(list(map(int, nums)))

with open("../data/p081_matrix.txt", "r") as f:
    data = []
    for line in f:
        line = line.strip().split(',')
        data.append(list(map(int, line)))

def p81(grid):
    print(grid)
    gridSize = len(grid[0])
    for i in range(gridSize-2, 0, -1):
        print(i)
        grid[gridSize-1][i] += grid[gridSize - 1][i+1]
        grid[i][gridSize-1] += grid[i+1][gridSize-1]

    for i in range(gridSize-2, 0, -1):
        for j in range(gridSize-2, 0 , -1):
            print('i,j', i,j)
            grid[i][j] += min(grid[i+1][j], grid[i][j+1])
    print(grid)
    return grid[-1][-1]

print(p81(test_data))




