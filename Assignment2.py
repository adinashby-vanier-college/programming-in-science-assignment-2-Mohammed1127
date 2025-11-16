def max_two_in_list(numbers):
    num_1 = max(numbers)
    while num_1 in numbers:
        numbers.remove(num_1)
    if numbers == []:
        return(num_1, None)
    else:
        num_2 = max(numbers)
    return (num_1, num_2)


def remove_duplicates_and_sort(numbers):
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)
    unique.sort()
    return unique


def cumulative_sum(arr):
    result = []
    running = 0
    for num in arr:
        running += num
        result.append(running)
    return result


def transpose_matrix(matrix):
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        result.append(new_row)
    return result


def slice_every_nth(lst, step):
    if step <= 0:
        return []
    result = []
    for i in range(0, len(lst), step):
        result.append(lst[i])
    return result


def dot_product(list1, list2):
    if len(list1) != len(list2):
        return None
    total = 0
    for a, b in zip(list1, list2):
        total += a * b
    return total


def matrix_multiplication(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    if cols1 != rows2:
        return None
    result = []
    for i in range(rows1):
        row = []
        for j in range(cols2):
            val = 0
            for k in range(cols1):
                val += matrix1[i][k] * matrix2[k][j]
            row.append(val)
        result.append(row)
    return result
