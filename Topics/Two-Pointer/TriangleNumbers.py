
from Tools.PrintPointers import *

"""
Valid Triangles - MEDIUM

https://leetcode.com/problems/valid-triangle-number
https://www.hellointerview.com/learn/code/two-pointers/valid-triangle-number

Given an integer array nums, return the number of triplets chosen from the array that can make 
triangles if we take them as side lengths of a triangle.

Example 1:
Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Example 2:
Input: nums = [4,2,3,4]
Output: 4
 

Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 1000
"""


def Solution1(nums):
    nums.sort()
    results = 0

    for i in range(len(nums) - 1, 1, -1):
        left = 0
        right = i - 1
        while left < right:
            if nums[i] < nums[left] + nums[right]:
                results += right - left
                right -= 1
            else:
                left += 1
    return results


if __name__ == "__main__":
    cases = [
        [[11, 4, 9, 6, 15, 18], 10],
        [[4, 2, 3, 1], 1],
        [[1, 1, 1, 1], 4],

        [[0, 0, 0], 0],
        [[3, 4, 6, 7], 3],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1]):
            output = solution(nums=deepcopy(case[0]))
            if output != case[1]:
                print(f'Failed   Solution {idx + 1}')
                print(f'Case: {case[0]}, Expected: {case[1]}, Got: {output}')

    print('-' * 150)
    print('Passed all test cases')
