
from collections import deque

from Tools.PrintPointers import *


"""
Search in Rotated Sorted Array - MEDIUM



"""


def Solution1(nums, k):
    window = nums[:k]
    maximums = [max(window)]

    if len(nums) == k:
        return maximums

    for i in range(1, len(nums) - k + 1):
        window = nums[i:i+k]
        maximums.append(max(window))
    return maximums


def Solution2(nums, k):

    queue = deque([])


    maximums = [max(nums[:k])]

    return maximums


if __name__ == "__main__":
    cases = [
        [[1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]],
        [[1], 1, [1]],
        [[9, 11], 2, [11]],

        [[4, -2], 2, [4]],
        [[1, 3, 1, 2, 0, 5], 3, [3, 3, 2, 5]],
        [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 4, [10, 9, 8, 7, 6, 5, 4]],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1]):
            output = solution(nums=deepcopy(case[0]), k=case[1])
            if output != case[2]:
                print(f'Failed   Solution {idx + 1}')
                print(f'Case: {case[0]}, Expected: {case[2]}, Got: {output}')

    print('-' * 150)
    print('Passed all test cases')
