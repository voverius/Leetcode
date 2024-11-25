
from Tools.PrintPointers import *


"""
Maximum Sum of Sub-arrays - EASY

Given an array of integers nums and an integer k, find the maximum sum of any contiguous subarray of size k.

EXAMPLES
Example 1: Input:

nums = [2, 1, 5, 1, 3, 2]
k = 3
Output:

9
Explanation: The subarray with the maximum sum is [5, 1, 3] with a sum of 9.
"""


def Solution1(nums, k):
    if k >= len(nums):
        return sum(nums)

    rolling = sum(nums[:k])
    sums = {rolling}

    for i in range(k, len(nums)):
        rolling += (nums[i] - nums[i - k])
        sums.add(rolling)
    return max(sums)


if __name__ == "__main__":
    cases = [
        [[2, 1, 5, 1, 3, 2], 3, 9],
        [[2, 3, 4, 1, 5], 2, 7],
        [[1, 1, 1, 1, 1], 2, 2],

        [[-1, -2, -3, -4], 2, -3],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 40],
        [[5, 2, -1, 0, 3], 3, 6],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1]):
            output = solution(nums=deepcopy(case[0]), k=case[1])
            if output != case[2]:
                print(f'Failed   Solution {idx + 1}')
                print(f'Case: {case[0]}, Expected: {case[2]}, Got: {output}')

    print('-' * 150)
    print('Passed all test cases')
