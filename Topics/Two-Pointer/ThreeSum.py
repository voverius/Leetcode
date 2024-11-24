
from Tools.PrintPointers import *

"""
Three Sum - Medium

https://leetcode.com/problems/3sum
https://www.hellointerview.com/learn/code/two-pointers/3-sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""


def Solution1(nums):
    values = set()
    nums.sort()
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        if nums[i] > 0:
            break

        while left < right:
            value = nums[left] + nums[right]
            if value == -nums[i]:
                values.add(tuple([nums[i], nums[left], nums[right]]))
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif nums[left] > -nums[i]:
                break
            elif value < -nums[i]:
                left += 1
            else:
                right -= 1
    return [list(value) for value in values]


def Solution2(nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result


def Solution3(nums):
    answer = []
    counter = {}
    for num in nums:
        counter[num] = 1 if num not in counter else counter[num] + 1
    if 0 in counter and counter[0] > 2:
        answer.append([0, 0, 0])
    for key in counter:
        if key != 0 and counter[key] > 1 and -2 * key in counter:
            temp = [key, key, -2 * key]
            temp.sort()
            answer.append(temp)
    keys = sorted(counter.keys())
    for i, num1 in enumerate(keys):
        if num1 > 0:
            break
        for num2 in keys[i + 1:]:
            diff = -num1 - num2
            if diff <= num2:
                break
            elif diff in counter:
                temp = [num1, num2, diff]
                temp.sort()
                answer.append(temp)
    return answer


if __name__ == "__main__":
    cases = [
        [[-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]],
        [[0, 1, 1], []],
        [[0, 0, 0], [[0, 0, 0]]],

        [[-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]],
        [[-1, -1, -1, 2, 2], [[-1, -1, 2]]],
        [[-4, -2, -1, 0, 1, 2, 3, 4], [[-4, 0, 4], [-4, 1, 3], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]]
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1, Solution2, Solution3]):
            output = solution(nums=deepcopy(case[0]))
            if output != case[1]:
                for subOutput in case[1]:
                    if subOutput not in output:
                        print(f'Failed   Solution {idx + 1}')
                        print(f'Case: {case[0]}, Missing: {subOutput}')

    print('-' * 150)
    print('Passed all test cases')
