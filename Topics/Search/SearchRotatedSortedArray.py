
from Tools.PrintPointers import *


"""
Search in Rotated Sorted Array - MEDIUM

https://leetcode.com/problems/search-in-rotated-sorted-array/description/
https://www.hellointerview.com/learn/code/binary-search/search-in-rotated-sorted-array


There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot 
index k (1 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target 
if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
 

Constraints:
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-10^4 <= target <= 10^4
"""


def Solution1(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < nums[left]:
            if target >= nums[left] or target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        elif nums[mid] > nums[right]:
            if target > nums[mid] or target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    cases = [
        [[4, 5, 6, 7, 0, 1, 2], 0, 4],
        [[4, 5, 6, 7, 0, 1, 2], 3, -1],
        [[4, 5, 6, 7, 0, 1, 2], 5, 1],
        [[4, 5, 6, 7, 8, 1, 2, 3], 8, 4],
        [[1], 0, -1],

        [[1, 3], 3, 1],
        [[3, 1], 1, 1],
        [[5, 1, 3], 5, 0],
        [[1, 3, 5], 5, 2],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1]):
            output = solution(nums=deepcopy(case[0]), target=case[1])
            if output != case[2]:
                print(f'Failed   Solution {idx + 1}')
                print(f'Case: {case[0]}, Expected: {case[2]}, Got: {output}')

    print('-' * 150)
    print('Passed all test cases')
