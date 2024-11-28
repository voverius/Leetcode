
from Tools.PrintPointers import *


"""
Spiral Matrix - MEDIUM

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


def Solution1(matrix):

    spiral = []
    m = len(matrix)
    n = len(matrix[0])

    if n == 1:
        return [row[0] for row in matrix]

    for i in range(m // 2 + 1):
        if i == m // 2 and not m % 2 or len(spiral) == n * m:
            break

        row = matrix[i] if i == 0 else matrix[i][i:-i]
        spiral.extend(row)

        if i == m // 2 and m % 2:
            break

        j = i + 1
        col1 = [row[-i - 1] for row in matrix[j:-j]]
        spiral.extend(col1)

        row = matrix[-i - 1] if i == 0 else matrix[-i - 1][i:-i]
        spiral.extend(row[::-1])

        if j > n / 2:
            break

        col2 = [row[i] for row in matrix[j:-j]]
        spiral.extend(col2[::-1])
    return spiral


if __name__ == "__main__":
    cases = [
        [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]],
        [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]],
        [[[1]], [1]],

        [[[2, 5, 8],
          [4, 0, -1]],
         [2, 5, 8, -1, 0, 4]],
        [[[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16],
          [17, 18, 19, 20],
          [21, 22, 23, 24]],
         [1, 2, 3, 4, 8, 12, 16, 20, 24, 23, 22, 21, 17, 13, 9, 5, 6, 7, 11, 15, 19, 18, 14, 10]],
        [[[2, 3, 4],
          [5, 6, 7],
          [8, 9, 10],
          [11, 12, 13],
          [14, 15, 16]],
         [2, 3, 4, 7, 10, 13, 16, 15, 14, 11, 8, 5, 6, 9, 12]],
        [[[1, 11],
          [2, 12],
          [3, 13],
          [4, 14],
          [5, 15],
          [6, 16],
          [7, 17],
          [8, 18],
          [9, 19],
          [10, 20]],
         [1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2]],

        [[[1, 2], [3, 4]], [1, 2, 4, 3]],
        [[[1, 2, 3, 4]], [1, 2, 3, 4]],
        [[[1], [2], [3], [4]], [1, 2, 3, 4]],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1]):
            output = solution(matrix=deepcopy(case[0]))
            if output != case[1]:
                print(f'Failed   Solution {idx + 1}')
                print(f'Case: {case[0]}, Expected: {case[1]}, Got: {output}')

    print('-' * 150)
    print('Passed all test cases')
