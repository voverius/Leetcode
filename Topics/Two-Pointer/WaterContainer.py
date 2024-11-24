
from Tools.PrintPointers import *

"""
Container With Most Water - MEDIUM

https://leetcode.com/problems/container-with-most-water/description/
https://www.hellointerview.com/learn/code/two-pointers/container-with-most-water


You are given an integer array height of length n. There are n vertical lines drawn such that the
two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the
most water.

Return the maximum amount of water a container can store.


Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Example 2:
Input: height = [1,1]
Output: 1


Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""

def Solution1(height):
    left = 0
    right = len(height) - 1
    areas = []

    while left != right:
        areas.append(min(height[left], height[right]) * (right - left))
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return max(areas)


if __name__ == "__main__":
    cases = [
        [[1, 8, 6, 2, 5, 4, 8, 3, 7], 49],
        [[1, 1], 1],
        [[4, 3, 2, 1, 4], 16],

        [[1, 2, 1], 2],
        [[1, 2, 4, 3], 4],
        [[1, 2, 3, 4, 5, 25, 24, 3, 4], 24],
    ]

    for case in cases:
        for solution in [Solution1]:
            output = solution(height=deepcopy(case[0]))
            if output != case[1]:
                print(f'Failed   Solution {solution}')
                print(case[0])

    print('-' * 150)
    print('Passed all test cases')
