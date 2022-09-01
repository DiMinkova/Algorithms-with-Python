# Let’s define a connected area in a matrix as an area of cells in which there is a path
# between every two cells.
# Write a program to find all connected areas in a matrix.

class Area:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


def connected_area(r, c, ll):
    if r < 0 or r >= m  or c < 0 or c >= n :
        return 0
    if ll[r][c] == '*' or ll[r][c] == 'v':
        return 0

    ll[r][c] = 'v'
    result = 1
    result += connected_area(r + 1, c, ll)
    result += connected_area(r, c + 1, ll)
    result += connected_area(r - 1, c, ll)
    result += connected_area(r, c - 1, ll)
    return result

# test cases
import sys
from io import StringIO
test1 = """4
9
---*---*-
---*---*-
---*---*-
----*-*--"""
test2 = """5
10
*--*---*--
*--*---*--
*--*****--
*--*---*--
*--*---*--"""
sys.stdin = StringIO(test2)

# read data
m = int(input())
n = int(input())
ll = [list(input()) for _ in range(m)]
print(ll)

# to store detected area parameters
areas = []

# start explore matrix
for row in range(m):
    for col in range(n):
        size = connected_area(row, col, ll)
        if size == 0:
            continue
        areas.append(Area(row, col, size))

print(f"Total areas found: {len(areas)}")
for idx, area in enumerate(sorted(areas, key=lambda a: -a.size)):
    print(f"Area #{idx + 1} at ({area.row}, {area.col}), size: {area.size}")