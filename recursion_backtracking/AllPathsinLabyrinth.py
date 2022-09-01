# You are given a labyrinth. Your goal is to find all paths from the start (cell 0, 0)
# to the exit, marked with 'e'.
#     • Empty cells are marked with a dash '-'.
#     • Walls are marked with a star '*'.
# On the first line, you will receive the dimensions of the labyrinth.
# Next, you will receive the actual labyrinth.
# The order of the paths does not matter.

import sys
from io import StringIO

test1 = """3
3
---
-*-
--e"""
test2 = """3
5
-**-e
-----
*****"""
sys.stdin = StringIO(test1)


def path_labyrinth(r, c, matrix, direction, path):
    if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
        return

    if matrix[r][c] == '*':
        return

    if matrix[r][c] == 'v':
        return

    path.append(direction)

    if matrix[r][c] == 'e':
        print(''.join(path))
    else:
        matrix[r][c] = 'v'
        path_labyrinth(r, c + 1, matrix, 'R', path)
        path_labyrinth(r, c - 1, matrix, 'L', path)
        path_labyrinth(r + 1, c, matrix, 'D', path)
        path_labyrinth(r - 1, c, matrix, 'U', path)
        matrix[r][c] = '-'
    path.pop()


# read labyrinth
matrix = []
rows = int(input())
columns = int(input())
for _ in range(rows):
    matrix.append(list(input()))
print(matrix)


# start point
st_r = 0
st_c = 0

# start_promenade
path_labyrinth(st_r, st_c, matrix, '', [])
