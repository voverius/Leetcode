
import heapq

from Tools.PrintPointers import *


"""
Kth Largest Element in an Array - MEDIUM

https://leetcode.com/problems/kth-largest-element-in-an-array/description/

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?


Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
1 <= k <= nums.length <= 105
-10^4 <= nums[i] <= 10^4
"""


def Solution1(nums, k):
    heap = []
    for i in nums:
        heapq.heappush(heap, i)
        if len(heap) > k:
            heapq.heappop(heap)
    return heapq.heappop(heap)


def Solution2(nums, k):
    return sorted(nums)[-k]


if __name__ == "__main__":
    cases = [
        [[3, 2, 1, 5, 6, 4], 2, 5],
        [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4],
        [[1], 1, 1],
        [[-1, -1], 2, -1],
        [[-1, 2, 0], 1, 2],

        [[7, 10, 4, 3, 20, 15], 3, 10],
        [[1, 2, 3, 4, 5, 6], 6, 1],
        [[99, 99, 99, 99], 2, 99],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1, Solution2]):
            output = solution(nums=deepcopy(case[0]), k=case[1])
            if output != case[2]:
                print(f'Failed   Solution {idx + 1}')
                print(f'Case: {case[0]}, Expected: {case[2]}, Got: {output}')

    print('-' * 150)
    print('Passed all test cases')
