# Write a program that draws the figure below depending on n.
import sys
from io import StringIO


test1 = """2"""
test2 = """5"""
sys.stdin = StringIO(test2)


def recursiveDrawing(n):
    if n == 0:
        return

    print(st_symbol * n)
    recursiveDrawing(n - 1)
    print(end_symbol * (n))


n = int(input())
st_symbol = '*'
end_symbol = '#'

recursiveDrawing(n)

