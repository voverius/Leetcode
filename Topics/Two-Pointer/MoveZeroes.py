
from Tools.PrintPointers import *

"""
Move Zeroes - MEDIUM

https://leetcode.com/problems/move-zeroes/
https://www.hellointerview.com/learn/code/two-pointers/move-zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order 
of the non-zero elements.

Note that you must do this in-place without making a copy of the array.


Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
"""


def Solution1(nums):
    count = 0
    zero = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count += 1
            continue
        nums[zero] = nums[i]
        zero += 1

    for i in range(count):
        nums[-i - 1] = 0
    return nums


def Solution2(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
    return nums


if __name__ == "__main__":
    cases = [
        [[0, 1, 0, 3, 12], [1, 3, 12, 0, 0]],
        [[0, 0, 1], [1, 0, 0]],
        [[1, 2, 3, 4, 0, 0], [1, 2, 3, 4, 0, 0]],

        [[0, 0, 0], [0, 0, 0]],
        [[1, 0, 2, 0, 3], [1, 2, 3, 0, 0]],
        [[4, 5, 6], [4, 5, 6]],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1, Solution2]):
            output = solution(nums=deepcopy(case[0]))
            if output != case[1]:
                print(f'Failed   Solution {idx + 1}')
                print(f'Case: {case[0]}, Expected: {case[1]}, Got: {output}')

    print('-' * 150)
    print('Passed all test cases')
