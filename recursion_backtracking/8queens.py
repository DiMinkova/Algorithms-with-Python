def can_place(r, c, rows, cols, lefts, rights):
    if r in rows or c in cols or r-c in lefts or r+c in rights:
        return False
    return True


def put_queens(r, c, matrix, rows, cols, lefts, rights):
    matrix[r][c] = '*'
    rows.add(r)
    cols.add(c)
    lefts.add(r-c)
    rights.add(r + c)


def remove_queens(r, c, matrix, rows, cols, lefts, rights):
    matrix[r][c] = '-'
    rows.remove(r)
    cols.remove(c)
    lefts.remove(r - c)
    rights.remove(r + c)


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))
    print()


def place_queens(r, matrix, rows, cols, lefts, rights):
    if r == 8:
        cnt[0] += 1
        print_matrix(matrix)
        return
    for c in range(8):
        if can_place(r, c, rows, cols, lefts, rights):
            put_queens(r, c, matrix, rows, cols, lefts, rights)
            place_queens(r + 1, matrix, rows, cols, lefts, rights)
            remove_queens(r, c, matrix, rows, cols, lefts, rights)


cnt = [0]
matrix = []
[matrix.append( ['-'] * 8) for _ in range(8)]
print(matrix)
place_queens(0, matrix, set(), set(), set(), set())
print(cnt[0])
