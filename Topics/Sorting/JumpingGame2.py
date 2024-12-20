
from Tools.PrintPointers import *


"""
Jump Game II - MEDIUM
https://leetcode.com/problems/jump-game-ii/description/

You are given a 0-indexed array of integers nums of length n. You are initially positioned at the 
first index, and each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.


Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, 
then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2


Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 1000
"""


def Solution1(nums):
    count = 0
    position = 0
    while True:
        if position >= len(nums) - 1:
            return count
        elif nums[position] + position >= len(nums) - 1:
            return count + 1
        elif nums[position] == 1:
            position += 1
        else:
            nextPos = position + 1
            maxPos = position + nums[position]
            for i in range(position + 1, maxPos + 1):
                value = i + nums[i]
                if i + nums[i] > maxPos:
                    nextPos = i
                    maxPos = value
            position = nextPos
        count += 1
    return


if __name__ == "__main__":
    cases = [
        [[2, 3, 1, 1, 4], 2],
        [[2, 3, 0, 1, 4], 2],
        [[1, 2, 1, 1, 1], 3],

        [[10, 1, 1, 1], 1],
        [[1, 1, 1, 1, 1], 4],
        [[5, 9, 3, 2, 1, 0, 3, 3, 3, 1], 2],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1]):
            output = solution(deepcopy(case[0]))
            if output != case[1]:
                print(f'Failed   Solution {idx + 1}')
                print(f'Case: {case[0]}, Expected: {case[1]}, Got: {output}')

    print('-' * 150)
    print('Passed all test cases')
