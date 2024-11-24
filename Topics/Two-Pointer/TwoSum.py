
from Tools.PrintPointers import *

"""
Two Sum - EASY

Given an array of integers nums and an integer target, return indices of the two numbers such that 
they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element 
twice.

You can return the answer in any order.


Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
"""


def Solution1(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return


def Solution2(nums, target):
    numMap = {}
    n = len(nums)

    for i in range(n):
        diff = target - nums[i]
        if diff in numMap:
            return [numMap[diff], i]
        numMap[nums[i]] = i
    return


def Solution3(nums, target):
    indexes = [(num, i) for i, num in enumerate(nums)]
    indexes.sort()

    left = 0
    right = len(nums) - 1

    while left < right:
        current = indexes[left][0] + indexes[right][0]
        if current == target:
            result = [indexes[left][1], indexes[right][1]]
            result.sort()
            return result
        elif current < target:
            left += 1
        else:
            right -= 1
    return


if __name__ == "__main__":
    cases = [
        [[2, 7, 11, 15], 9, [0, 1]],
        [[3, 2, 4], 6, [1, 2]],
        [[3, 3], 6, [0, 1]],

        [[1, 2, 3, 4, 5], 9, [3, 4]],
        [[-1, -2, -3, -4, -5], -8, [2, 4]],
        [[0, 4, 3, 0], 0, [0, 3]],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1, Solution2, Solution3]):
            output = solution(nums=deepcopy(case[0]), target=case[1])
            if output != case[2]:
                print(f'Failed   Solution {idx + 1}')
                print(case[0])

    print('-' * 150)
    print('Processed all test cases')
