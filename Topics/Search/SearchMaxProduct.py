
from Tools.PrintPointers import *


"""
Maximum Product Subarray - MEDIUM

https://leetcode.com/problems/maximum-product-subarray/description/

Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.


Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Constraints:
1 <= nums.length <= 2 * 10^4
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""


def Solution1(nums):
    if len(nums) == 1:
        return nums[0]
    left = 1
    right = 1
    maximums = set()
    for i in range(len(nums)):
        left *= nums[i]
        maximums.add(left)
        if left == 0:
            left = 1
        right *= nums[len(nums) - i - 1]
        maximums.add(right)
        if right == 0:
            right = 1
    return max(maximums)


if __name__ == "__main__":
    cases = [
        [[2, -2, 6, 8, 0, 2], 48],
        [[2, 3, -2, 4], 6],
        [[2, -5, -2, -4, 3], 24],
        [[-2, 0, -1], 0],
        [[-2, 3, -4], 24],

        [[0, 2], 2],
        [[-2, -3, -4], 12],
        [[1, 2, 3, 4], 24],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1]):
            output = solution(nums=deepcopy(case[0]))
            if output != case[1]:
                print(f'Failed   Solution {idx + 1}')
                print(f'Case: {case[0]}, Expected: {case[1]}, Got: {output}')

    print('-' * 150)
    print('Passed all test cases')
