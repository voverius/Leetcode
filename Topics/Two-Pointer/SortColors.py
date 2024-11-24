
from Tools.PrintPointers import *


"""
Sort Colors - MEDIUM

https://leetcode.com/problems/sort-colors
https://www.hellointerview.com/learn/code/two-pointers/sort-colors


Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects
of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.


Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
"""


def Solution1(nums):
    """This is a hash table solution"""
    if len(nums) == 1:
        return nums

    counter = {0: 0, 1: 0, 2: 0}
    for num in nums:
        counter[num] += 1

    index = 0
    if counter[0]:
        index += counter[0]
        nums[0:index] = [0] * counter[0]
    if counter[1]:
        nums[index:(index + counter[1])] = [1] * counter[1]
        index += counter[1]
    if counter[2]:
        nums[index:] = [2] * counter[2]
    return nums


def Solution2(nums):
    """This is a 2 pointer solution"""
    left, right = 0, len(nums) - 1
    i = 0

    while i <= right:
        if nums[i] == 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
        else:
            i += 1
    return nums


if __name__ == "__main__":
    cases = [
        [[2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]],
        [[0, 1, 2, 1, 0], [0, 0, 1, 1, 2]],
        [[1, 2, 0, 1, 2, 0], [0, 0, 1, 1, 2, 2]],

        [[0], [0]],
        [[1, 1, 1, 1], [1, 1, 1, 1]],
        [[2, 2, 1, 1, 0, 0], [0, 0, 1, 1, 2, 2]],
    ]

    for case in cases:
        for solution in [Solution1, Solution2]:
            output = solution(nums=deepcopy(case[0]))
            if output != case[1]:
                print(f'Failed   Solution {solution}')
                print(case[0])

    print('-' * 150)
    print('Passed all test cases')
