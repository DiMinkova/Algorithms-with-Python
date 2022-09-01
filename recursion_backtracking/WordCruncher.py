# Let’s define a connected area in a matrix as an area of cells in which there is a
# path between every two cells.
# Write a program to find all connected areas in a matrix.
# Input
#     On the first line, you will get the number of rows.
#     On the second line, you will get the number of columns.
#     The rest of the input will be the actual matrix.
# Output
# Print each of them found ways to form the required string as shown
# in the examples


# test cases
import sys
from io import StringIO

test1 = """text, me, so, do, m, ran, y
somerandomtext"""

test2 = """Word, cruncher, cr, h, unch, c, r, un, ch, er
Wordcruncher"""

test3 = """tu, stu, p, i, d, pi, pid, s, pi
stupid"""

sys.stdin = StringIO(test2)

# read & manipulate data.
# for each word find the eventual place of the word in the target sentence.

# read input data
words = input().split(', ')
target = input()

# manipulate & storing data in two dictionaries
words_places = {}
words_count = {}

for word in words:
    if word not in target:
        continue

    if word not in words_count:
        words_count[word] = 0
    words_count[word] += 1

    try:
        idx = 0
        while True:
            idx = target.index(word, idx)
            if idx not in words_places:
                words_places[idx] = []
            words_places[idx].append(word)
            idx += len(word)
    except ValueError:
        pass

print(words_count)
print(words_places)


# recursive function to find solutions
def find_solutions(ind, words_count, words_places, result):
    if ind >= len(target):
        print('-'.join(result))
        return

    if ind not in words_places:
        return

    for word in words_places[ind]:
        result.append(word)
        words_count[word] -= 1

        find_solutions(ind + len(word), words_count, words_places, result)

        result.pop()
        words_count[word] += 1


find_solutions(0, words_count, words_places,[])






