# One of the simplest strategies for searching data is to simply loop through each element
# looking for the target. Each data point is searched for a match and when a match is found,
# the results are returned and the algorithm exits the loop. Otherwise, the algorithm keeps
# on searching until it reaches the end of the data. The obvious disadvantage of linear search
# is that it is very slow due to the inherent exhaustive search. The advantage is that the data
# does not need to be sorted, as required by the other algorithms presented in this chapter.


def linear_search(list, item):
    index = 0
    found = False
# Match the value with each data element
    while index < len(list) and found is False:
        if list[index] == item:
            found = True
        else:
            index = index + 1
    return found


list = [6, 8, 4, 'g','h']
print(linear_search(list, 'g'))
print(linear_search(list, 3))


# The pre-requisite of the binary search algorithm is sorted data.
# The algorithm iteratively divides a list into two parts and keeps a track of the lowest and highest
# indices until it finds the value it is looking for:

def binary_search(list, item):
    first = 0
    last = len(list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if list[midpoint] == item:
            found = True
        else:
            if item < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


list = [-6, -5, -4, 0, 3, 9, 17, 56, 62, 65]
print(binary_search(list, -5))
print(binary_search(list, 76))

