
from Tools.PrintPointers import *


"""
Remove Duplicates from Sorted Array II - MEDIUM

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that 
each unique element appears at most twice. The relative order of the elements should be kept the same.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place 
with O(1) extra memory.


Example 1:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2, 
and 3. It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums containing 0, 0, 
1, 1, 2, 3, and 3. Note that the five elements can be returned in any order.


Constraints:
1 <= nums.length <= 3 * 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.
"""


def Solution1(nums):
    seen = {}
    position = 0

    for num in nums:
        seen[num] = seen.get(num, 0) + 1
        if seen[num] <= 2:
            nums[position] = num
            position += 1
    return position


def Solution2(nums):
    position = 0
    while position < len(nums) - 2:
        if nums[position] == nums[position + 2]:
            nums.pop(position + 2)
            continue
        position += 1
    return len(nums)


if __name__ == "__main__":
    cases = [
        [[1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3]],
        [[0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3]],
        [[1], 1, [1]],

        [[1, 1, 1, 1], 2, [1, 1]],
        [[1, 2, 3, 3, 3], 4, [1, 2, 3, 3]],
        [[-1, -1, 0, 0, 0, 1], 5, [-1, -1, 0, 0, 1]],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1]):
            nums_copy = deepcopy(case[0])
            k = solution(nums=nums_copy)
            if k != case[1] or nums_copy[:k] != case[-1]:
                print(f'Failed   Solution {idx + 1}')
                print(f'Case: {case[0]}, Expected: k={case[1]}, nums={case[-1]}, Got: k={k}, nums={nums_copy[:k]}')

    print('-' * 150)
    print('Passed all test cases')


