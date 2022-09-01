## Write a program that simulates the execution of n nested loops from 1 to n
# which prints the values of all its iteration variables at any given time on
# a single line. Use recursion.

def recursively_call_nested_loop(i, ll):
    if i >= n:
        print(" ".join(str(x) for x in ll))
        return

    for symbol in range(1, n + 1):
        ll[i] = symbol
        recursively_call_nested_loop(i + 1, ll)


n = int(input())
ll = [0] * n
recursively_call_nested_loop(0, ll)

