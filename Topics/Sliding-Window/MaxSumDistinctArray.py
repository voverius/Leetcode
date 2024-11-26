
from Tools.PrintPointers import *


"""
Maximum Sum of Distinct Sub-arrays With Length K - MEDIUM

https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k
https://www.hellointerview.com/learn/code/sliding-window/maximum-sum-of-distinct-subarrays-with-length-k

You are given an integer array nums and an integer k. Find the maximum subarray sum of all the 
sub-arrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the sub-arrays that meet the conditions. If no subarray 
meets 
the conditions, return 0.

A sub-array is a contiguous non-empty sequence of elements within an array.


Example 1:
Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The sub-arrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the sub-arrays that meet the conditions

Example 2:
Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The sub-arrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no sub-arrays meet the conditions.


Constraints:
1 <= k <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""


def Solution1(nums, k):

    seen = {}
    left = 0
    sums = {0}
    rolling = 0

    for right in range(len(nums)):
        seen[nums[right]] = seen.get(nums[right], 0) + 1
        rolling += nums[right]

        while seen[nums[right]] > 1:
            seen[nums[left]] -= 1
            rolling -= nums[left]
            left += 1

        if right - left == k - 1:
            sums.add(rolling)
            seen[nums[left]] -= 1
            rolling -= nums[left]
            left += 1
    return max(sums)


def Solution2(nums, k):

    rolling = sum(nums[:k])
    seen = {num: i for i, num in enumerate(nums[:k])}
    sums = {0} if len(seen) < k else {rolling}

    for right in range(k, len(nums)):
        left = right - k
        rolling += nums[right] - nums[left]
        seen[nums[right]] = right
        PrintPointers(nums, left, right)

        if seen[nums[left]] == left:
            del seen[nums[left]]
        if len(seen) == k:
            sums.add(rolling)
    return max(sums)


if __name__ == "__main__":
    cases = [
        [[3, 2, 2, 3, 4, 6, 7, 7, -1], 4, 20],
        [[1, 2, 3, 4, 5], 3, 12],
        [[4, 4, 4, 4], 2, 0],

        [[1, 2, 1, 3, 4], 3, 8],
        [[5, 5, 5, 5, 5], 1, 5],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 40],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1, Solution2]):
            output = solution(nums=deepcopy(case[0]), k=case[1])
            if output != case[2]:
                print(f'Failed   Solution {idx + 1}')
                print(f'Case: {case[0]}, Expected: {case[2]}, Got: {output}')

    print('-' * 150)
    print('Passed all test cases')
