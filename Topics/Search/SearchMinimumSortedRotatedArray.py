

from Tools.PrintPointers import *


"""
Search in Rotated Sorted Array - MEDIUM

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array 
[a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.


Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""


def Solution1(nums):

    left = 0
    right = len(nums) - 1
    values = set()

    while left <= right:
        mid = (right + left) // 2
        value = nums[mid]
        if value < nums[left]:
            values.add(value)
            right = mid - 1
        elif value > nums[right]:
            left = mid + 1
        else:
            values.add(nums[left])
            break
    return min(values)


if __name__ == "__main__":
    cases = [
        [[3, 4, 5, 1, 2], 1],
        [[4, 5, 6, 7, 0, 1, 2], 0],
        [[11, 13, 15, 17], 11],
        [[4, 1, 2], 1],

        [[2, 1], 1],
        [[1], 1],
        [[5, 6, 7, 8, 9, 1, 2, 3, 4], 1],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1]):
            output = solution(nums=deepcopy(case[0]))
            if output != case[1]:
                print(f'Failed   Solution {idx + 1}')
                print(f'Case: {case[0]}, Expected: {case[1]}, Got: {output}')

    print('-' * 150)
    print('Passed all test cases')
