
from Tools.PrintPointers import *


"""
Maximum Points You Can Obtain from Cards - MEDIUM

https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
https://www.hellointerview.com/learn/code/sliding-window/maximum-points-you-can-obtain-from-cards

There are several cards arranged in a row, and each card has an associated number of points. The 
points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take 
exactly k cards.

Your score is the sum of the points of the cards you have taken.
Given the integer array cardPoints and the integer k, return the maximum score you can obtain.


Example 1:
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card 
first will maximize your total score. The optimal strategy is to take the three cards on the right, 
giving a final score of 1 + 6 + 5 = 12.

Example 2:
Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.

Example 3:
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
 

Constraints:
1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length
"""


def Solution1(cardPoints, k):
    if k >= len(cardPoints):
        return sum(cardPoints)

    eligible = cardPoints[-k:] + cardPoints[:k]
    rolling = sum(eligible[:k])
    sums = {rolling}
    for i in range(k, len(eligible)):
        rolling += (eligible[i] - eligible[i - k])
        sums.add(rolling)
    return max(sums)


def Solution2(cardPoints, k):
    if k >= len(cardPoints):
        return sum(cardPoints)

    rolling = sum(cardPoints[:k])
    sums = {rolling}
    for i in range(k - 1, -1, -1):
        rolling += cardPoints[i - k]
        rolling -= cardPoints[i]
        sums.add(rolling)
    return max(sums)


if __name__ == "__main__":
    cases = [
        [[1, 2, 3, 4, 5, 6, 1], 3, 12],
        [[2, 2, 2], 2, 4],
        [[9, 7, 7, 9, 7, 7, 9], 7, 55],

        [[1, 1000, 1], 1, 1],
        [[1, 79, 80, 1, 1, 1, 200, 1], 3, 202],
        [[100, 40, 17, 9, 73, 75], 3, 248],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1, Solution2]):
            output = solution(cardPoints=deepcopy(case[0]), k=case[1])
            if output != case[2]:
                print(f'Failed   Solution {idx + 1}')
                print(f'Case: {case[0]}, Expected: {case[2]}, Got: {output}')

    print('-' * 150)
    print('Passed all test cases')
