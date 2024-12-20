
from Tools.PrintPointers import *


"""
Remove Duplicates from Sorted Array - EASY

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that 
each unique element appears only once. The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following 
things:
1. Change the array nums such that the first k elements of nums contain the unique elements in the order 
   they were present in nums initially. The remaining elements of nums are not important as well as the 
   size of nums.
2. Return k.

Do not allocate extra space for another array. You must do this by modifying the input array in-place 
with O(1) extra memory.


Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 
respectively. It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 1, 
2, 3, and 4. Note that the five elements can be returned in any order.


Constraints:
1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""


def Solution1(nums):

    value = nums[0]
    position = 1

    for num in nums[1:]:
        if num != value:
            nums[position] = num
            value = num
            position += 1
    return position


if __name__ == "__main__":
    cases = [
        [[1, 1, 2], 2, [1, 2]],
        [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]],
        [[1], 1, [1]],

        [[1, 1, 1], 1, [1]],
        [[1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]],
        [[-1, 0, 0, 0, 3], 3, [-1, 0, 3]],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1]):
            nums_copy = deepcopy(case[0])
            k = solution(nums=nums_copy)
            if k != case[1] or nums_copy[:k] != case[-1]:
                print(f'Failed   Solution {idx + 1}')
                print(f'Case: {case[0]}, Expected: k={case[1]}, nums={case[-1]}, '
                      f'Got: k={k}, nums={nums_copy[:k]}')

    print('-' * 150)
    print('Passed all test cases')
