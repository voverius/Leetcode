
from Tools.PrintPointers import *


"""
Best Time to Buy and Sell Stock II - MEDIUM

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of 
the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.


Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock.


Constraints:
1 <= prices.length <= 3 * 10^4
0 <= prices[i] <= 10^4
"""


def Solution1(prices):
    profits = 0
    for i in range(len(prices) - 1):
        diff = prices[i + 1] - prices[i]
        if diff > 0:
            profits += diff
    return profits


if __name__ == "__main__":
    cases = [
        [[7, 1, 5, 3, 6, 4], 7],
        [[1, 2, 3, 4, 5], 4],
        [[7, 6, 4, 3, 1], 0],

        [[1, 10, 1, 10], 18],
        [[5, 5, 5, 5], 0],
        [[1, 2, 10, 3, 5], 11],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1]):
            output = solution(deepcopy(case[0]))
            if output != case[1]:
                print(f'Failed   Solution {idx + 1}')
                print(f'Case: {case[0]}, Expected: {case[1]}, Got: {output}')

    print('-' * 150)
    print('Passed all test cases')
