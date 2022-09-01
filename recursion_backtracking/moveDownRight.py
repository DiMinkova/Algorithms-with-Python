# Marinette has the ability to transform into Ladybug. She is stuck on a grid.
# Her initial location is at the top-left
# corner and tries to move to the bottom-right corner. However, she can only move either down or right
# at any point in time.
# Write a program that prints the number of all possible unique paths that Marinette can
# take to reach the bottom-right corner.
# Print the number of all possible unique paths to the bottom-right corner.

# test cases
import sys
from io import StringIO
test1 = """3
2"""
test2 = """2
3"""
sys.stdin = StringIO(test2)

# read data
m = int(input())
n = int(input())
ll = [['-'] * n for _ in range(m)]
print(ll)

# count possible path
cnt = [0]


# define base of recursion
# visit cells
# recursive call to
# unmarked cell
def recursive_move_r_d(row, col, ll):
    if row == m - 1 and col == n - 1:
        cnt[0] += 1
        return
    if row >= m or col >= n or ll[row][col] == 'v':
        return

    ll[row][col] = 'v'
    recursive_move_r_d(row + 1, col, ll)
    recursive_move_r_d(row, col + 1, ll)
    ll[row][col] = '-'


# call function
recursive_move_r_d(0, 0, ll)
print(cnt[0])



