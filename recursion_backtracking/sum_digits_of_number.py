# find sum of digits of any positive integer number

def recursive_sum(num):
    assert num >= 0 and isinstance(num, int), 'Must be positive integer number '
    if len(str(num)) <= 2:
       return num // 10  + num % 10

    return recursive_sum(num // 10) + num % 10


number = int(input())
print(recursive_sum(number))