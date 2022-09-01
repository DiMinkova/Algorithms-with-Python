# Generate all n-bit vectors of 0 and 1 in lexicographic order.
import sys
from io import StringIO


test1 = """2"""
test2 = """5"""
sys.stdin = StringIO(test2)


def generating_vectors(n, matrix, cnt):
    if n >= len(matrix):
        cnt[0] += 1
        print(''.join(str(x) for x in matrix))
        return
    for ind in range(2):
        matrix[n] = ind
        generating_vectors(n + 1, matrix, cnt)


cnt = [0]
n = int(input())
matrix = [None] * n
print(matrix)

generating_vectors(0, matrix, cnt)
print(cnt)
