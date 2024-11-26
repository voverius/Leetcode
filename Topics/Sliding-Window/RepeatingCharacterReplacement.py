
from Tools.PrintPointers import *


"""
Longest Repeating Character Replacement - MEDIUM

https://leetcode.com/problems/longest-repeating-character-replacement/description/
https://www.hellointerview.com/learn/code/sliding-window/longest-repeating-character-replacement

You are given a string s and an integer k. You can choose any character of the string and change it 
to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing 
the above operations.


Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:
1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length
"""


def Solution1(s, k):
    seen = {}
    left = 0
    lengths = {0}
    currentBest = 0

    for right in range(len(s)):
        seen[s[right]] = seen.get(s[right], 0) + 1
        currentBest = max(currentBest, seen[s[right]])
        length = right - left + 1
        if currentBest + k >= length:
            lengths.add(length)
            continue
        seen[s[left]] -= 1
        left += 1
    return max(lengths)


if __name__ == "__main__":
    cases = [
        ["ABAB", 2, 4],
        ["AABABBA", 1, 4],
        ["AAAA", 2, 4],

        ["ABCD", 1, 2],
        ["BBABCCDD", 2, 5],
        ["AABACCCBAABBCCAAABBACCCBAA", 3, 7],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1]):
            output = solution(s=deepcopy(case[0]), k=case[1])
            if output != case[2]:
                print(f'Failed   Solution {idx + 1}')
                print(f'Case: {case[0]}, Expected: {case[2]}, Got: {output}')

    print('-' * 150)
    print('Passed all test cases')
