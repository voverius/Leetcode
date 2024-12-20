
from Tools.PrintPointers import *


"""
Search a 2D Matrix - MEDIUM

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.


Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true


Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
"""


def Solution1(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    left = 0
    right = rows * cols - 1

    while left <= right:
        mid = left + (right - left) // 2
        row = mid // cols
        col = mid % cols

        value = matrix[row][col]
        if value > target:
            right = mid - 1
        elif value < target:
            left = mid + 1
        else:
            return True
    return False


if __name__ == "__main__":
    cases = [
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True],
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False],
        [[[1]], 1, True],

        [[[1, 3]], 3, True],
        [[[1, 3]], 2, False],
        [[[1, 3, 5, 7], [10, 11, 16, 20]], 20, True],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1]):
            output = solution(matrix=deepcopy(case[0]), target=case[1])
            if output != case[2]:
                print(f'Failed   Solution {idx + 1}')
                print(f'Case: {case[0]}, Expected: {case[2]}, Got: {output}')

    print('-' * 150)
    print('Passed all test cases')
