
from Tools.PrintPointers import *


"""
Remove Element - EASY

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have 
the result be placed in the first part of the array nums. More formally, if there are k elements 
after removing the duplicates, then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place 
with O(1) extra memory.


Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 
0, 1, 3, 0, and 4. Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""


def Solution1(nums, val):
    count = 0
    position = 0

    for num in nums:
        if num == val:
            count += 1
        else:
            nums[position] = num
            position += 1
    return len(nums) - count


if __name__ == "__main__":
    cases = [
        [[3, 2, 2, 3], 3, 2, [2, 2]],
        [[0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 4, 0, 3]],
        [[1], 1, 0, []],

        [[2, 2, 2], 2, 0, []],
        [[4, 5, 6], 7, 3, [4, 5, 6]],
        [[1, 2, 3, 4, 5], 3, 4, [1, 2, 4, 5]],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1]):
            nums_copy = deepcopy(case[0])
            k = solution(nums=nums_copy, val=case[1])
            if k != case[2] or sorted(nums_copy[:k]) != sorted(case[-1]):
                print(f'Failed   Solution {idx + 1}')
                print(f'Case: {case[0]}, Expected: k={case[2]}, nums={case[-1]}, '
                      f'Got: k={k}, nums={nums_copy[:k]}')

    print('-' * 150)
    print('Passed all test cases')
