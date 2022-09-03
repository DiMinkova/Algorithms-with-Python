#Pass 1 of Bubble Sort
# Due to two levels of looping, the worst-case runtime complexity would be O(n2).
# it should be used for smaller datasets.
# Bubble sort is based on various iterations, called passes. For a list of size N, bubble sort will have N-1 passes.
# Let's focus on the first iteration: pass one.
# The goal of pass one is pushing the highest value to the top of the list. We will see the highest value
# of the list bubbling its way to the top as pass one progresses.
# Bubble sort compares adjacent neighbor values. If the value at a higher position is higher in value
# than the value at a lower index, we exchange the values. This iteration continues until we reach the end
# of the list. This is shown in the following diagram:


def bubble_sort(list):
    lastElementIndex = len(list) - 1
    for i in range(lastElementIndex, 0, - 1):
        for idx in range(lastElementIndex):
            if list[idx]>list[idx+1]:
                list[idx],list[idx+1]=list[idx+1],list[idx]
    return list

list = [3, 62, 0, 65, 56, 17, -4]
bubble_sort(list)
print(list)


##################################
# The basic idea of insertion sort is that in each iteration, we remove a data point from the data structure
# we have and then insert it into its right position. That is why we call this the insertion sort algorithm.
# In the first iteration, we select the two data points and sort them. Then, we expand our selection and select
# the third data point and find its correct position, based on its value. The algorithm progresses until all the
# data points are moved to their correct positions.

def insert_sort(list):
    for i in range(len(list)):
        j = i
        while j > 0 and list[j] < list[j - 1]:
            list[j], list[j-1] = list[j - 1], list[j]
            j -= 1
    return list

list = [3, 62, 0, 65, 56, 17, -4, -5]
insert_sort(list)
print(list)

###################################
#Selection sort – simple, but inefficient algorithm
# Swap the first with the min element on the right, then the second, etc.
# Memory: O(1)
# Time: O(n2)
# Stable: No
# Method: Selection


def selection_sort(list):
    for ind in range(len(list)):
        min_ind = ind
        for curr_ind in range(ind + 1, len(list)):
            if list[min_ind] > list[curr_ind]:
                list[min_ind], list[curr_ind] = list[curr_ind], list[min_ind]


list = [3, 62, 0, 65, 56, 17, -4, -5, 9, - 6]
selection_sort(list)
print(list)


# Merge sort is efficient sorting algorithm
# Divide the list into sub-lists (typically 2 sub-lists)
# Sort each sub-list (recursively call merge-sort)
# Merge the sorted sub-lists into a single list
# Memory: O(n) / O(n*log(n))
# Time: O(n*log(n))
# Highly parallelizable on multiple cores / machines  up to O(log(n))



def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2  # splits list in half
        left = list[:mid]
        right = list[mid:]

        merge_sort(left)  # repeats untill len of each list is 1
        merge_sort(right)

        a = 0
        b = 0
        c = 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list[c] = left[a]
                a += 1
            else:
                list[c] = right[b]
                b += 1
            c += 1
        while a < len(left):
            list[c] = left[a]
            a += 1
            c += 1
        while b < len(right):
            list[c] = right[b]
            b += 1
            c += 1

    return list


list = [3, 62, 0, 65, 56, 17, -4, -5, 9, - 6]
merge_sort(list)
print(list)