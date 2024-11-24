
from Tools.PrintPointers import *

"""
Trap Rain Water - HARD

https://leetcode.com/problems/trapping-rain-water
https://www.hellointerview.com/learn/code/two-pointers/trapping-rain-water

Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

#xample 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array 
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
"""


def Solution1(height):
    if len(height) < 3:
        return 0

    results = 0
    maxIdx = len(height) - 1 - height[::-1].index(max(height))

    def ClimbUp(values):
        count = 0
        for left, value in enumerate(values):
            if value > 0:
                if left >= len(values) - 2:
                    return 0
                break
        else:
            return 0

        while left < len(values) - 2:
            temp = 0
            right = left + 1
            while right < len(values):
                if values[left] <= values[right]:
                    count += temp
                    temp = 0
                    left = right
                else:
                    temp += values[left] - values[right]
                right += 1
            left += 1
        return count

    if maxIdx > 1:
        results += ClimbUp(values=height[:maxIdx + 1])
    if maxIdx < len(height) - 2:
        results += ClimbUp(values=height[maxIdx:][::-1])
    return results


def Solution2(height):

    left = 0
    right = len(height) - 1
    leftMax = 0
    rightMax = 0
    results = 0

    while left < right:
        if height[left] <= height[right]:
            if height[left] >= leftMax:
                leftMax = height[left]
            else:
                results += leftMax - height[left]
            left += 1
        else:
            if height[right] >= rightMax:
                rightMax = height[right]
            else:
                results += rightMax - height[right]
            right -= 1
    return results


if __name__ == "__main__":
    cases = [
        [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6],
        [[3, 4, 1, 2, 2, 5, 1, 0, 2], 10],
        [[4, 2, 0, 3, 2, 5], 9],
        [[1, 0, 2, 0, 1], 2],

        [[0, 0, 0, 0], 0],
        [[1, 0], 0],
        [[3, 3, 3], 0],
        [[5, 4, 1, 2, 1, 3], 5],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1, Solution2]):
            output = solution(height=deepcopy(case[0]))
            if output != case[1]:
                print(f'Failed   Solution {idx + 1}')
                print(f'Case: {case[0]}, Expected: {case[1]}, Got: {output}')

    print('-' * 150)
    print('Passed all test cases')
