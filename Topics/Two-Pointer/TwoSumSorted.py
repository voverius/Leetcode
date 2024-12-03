
from Tools.PrintPointers import *

"""
Two Sum II - Input Array Is Sorted - MEDIUM

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two 
numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] 
and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, as an integer array [index1, index2] of 
length 2.

You may assume that each input would have exactly one solution, and you may not use the same element 
twice.


Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore, index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore, index1 = 1, index2 = 2. We return [1, 2].


Constraints:
2 <= numbers.length <= 3 * 10^4
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""


def Solution1(numbers, target):

    left = 0
    right = len(numbers) - 1

    while left < right:
        new = numbers[left] + numbers[right]
        if new == target:
            return [left + 1, right + 1]
        elif new < target:
            left += 1
        else:
            right -= 1
    return


if __name__ == "__main__":
    cases = [
        [[2, 7, 11, 15], 9, [1, 2]],
        [[2, 3, 4], 6, [1, 3]],
        [[-1, 0], -1, [1, 2]],

        [[1, 2, 3, 4, 5], 8, [3, 5]],
        [[-3, -2, -1, 0, 1, 2, 3], 0, [1, 7]],
        [[1, 1, 2, 2], 3, [1, 4]],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1]):
            output = solution(deepcopy(case[0]), deepcopy(case[1]))
            if output != case[2]:
                print(f'Failed   Solution {idx + 1}')
                print(f'Case: numbers={case[0]}, target={case[1]}, Expected: {case[2]}, Got: {output}')

    print('-' * 150)
    print('Passed all test cases')
