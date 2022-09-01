# Write a program that finds the sum of all elements in an integer array. Use recursion.
import sys
from io import StringIO
test1 = """1 2 3 4"""
test2 = """-1 0 1"""
sys.stdin = StringIO(test1)


def calc_sum(ll_data):
    ind = 0
    if ind >= len(ll_data) - 1:
        return ll_data[ind]
    while True:
        return ll_data[ind] + calc_sum(ll_data[ind+1:])
        ind += 1


def calc_sum_iterative(ll_data):
    suma = 0
    for numb in ll_data:
        suma += numb
    return suma


def reverse_recursively_array(ind, ll_data):
    n = len(ll_data) // 2
    m = len(ll_data)
    if ind >= n:
        return
    ll_data[ind], ll_data[m - 1 - ind] = ll_data[m - 1 - ind], ll_data[ind]
    reverse_recursively_array(ind + 1, ll_data)


ll_data = [int(x) for x in  input().split(' ')]
print(*ll_data)
print(calc_sum(ll_data))
print(calc_sum_iterative(ll_data))
reverse_recursively_array(0, ll_data)
print(' '.join(str(x) for x in ll_data))


