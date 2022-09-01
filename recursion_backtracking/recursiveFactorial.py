# Write a program that draws the figure below depending on n.
import sys
from io import StringIO


test1 = """5"""
test2 = """10"""
sys.stdin = StringIO(test2)


def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)


def fact_iterative(n):
    facta = 1
    for numb in range(n, 1, - 1):
        facta *= numb
    return facta


n = int(input())
print(fact(n))
print(fact_iterative(n))