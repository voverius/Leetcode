
from Tools.PrintPointers import *


"""
Merge Sorted Array - EASY

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers 
m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the 
array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote 
the elements that should be merged, and the last n elements are set to 0 and should be ignored. 
nums2 has a length of n.


Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge 
result can fit in nums1.
 

Constraints:
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-10^9 <= nums1[i], nums2[j] <= 10^9
"""


def Solution1(nums1, m, nums2, n):
    nums1[m:] = nums2
    nums1.sort()
    return nums1


def Solution2(nums1, m, nums2, n):
    first = m - 1
    second = n - 1
    final = len(nums1) - 1

    while second >= 0:
        if first >= 0 and nums1[first] >= nums2[second]:
            nums1[final] = nums1[first]
            first -= 1
            final -= 1
        else:
            nums1[final] = nums2[second]
            second -= 1
            final -= 1
    return nums1


if __name__ == "__main__":
    cases = [
        [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]],
        [[1], 1, [], 0, [1]],
        [[0], 0, [1], 1, [1]],

        [[4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]],
        [[1, 2, 4, 5, 6, 0], 5, [3], 1, [1, 2, 3, 4, 5, 6]],
        [[2, 0], 1, [1], 1, [1, 2]],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1, Solution2]):
            output = solution(nums1=deepcopy(case[0]),
                              m=case[1],
                              nums2=deepcopy(case[2]),
                              n=case[3])
            if output != case[-1]:
                print(f'Failed   Solution {idx + 1}')
                print(f'Case: {case[0]}, Expected: {case[-1]}, Got: {output}')

    print('-' * 150)
    print('Passed all test cases')
