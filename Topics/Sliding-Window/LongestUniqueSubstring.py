
from Tools.PrintPointers import *


"""
Longest Substring Without Repeating Characters - MEDIUM

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
https://www.hellointerview.com/learn/code/sliding-window/longest-substring-without-repeating-characters

Given a string s, find the length of the longest substring without repeating characters.


Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.

"""


def Solution1(s):
    if len(s) < 2:
        return len(s)
    n = len(s)
    lengths = {1}
    charMap = {}
    left = 0

    for right in range(n):
        if s[right] not in charMap or charMap[s[right]] < left:
            charMap[s[right]] = right
            lengths.add(right - left + 1)
        else:
            left = charMap[s[right]] + 1
            charMap[s[right]] = right
    return max(lengths)


def Solution2(s):
    if len(s) < 2:
        return len(s)

    left = 0
    right = 0
    lengths = {1}
    letters = {s[left]: 0}
    indexes = {0: s[left]}

    while right < len(s) - 1:
        right += 1
        if s[right] in letters:
            for i in range(left, letters[s[right]] + 1):
                letters.pop(indexes[i])
                indexes.pop(i)
                left += 1
        else:
            lengths.add(right - left + 1)
        indexes[right] = s[right]
        letters[s[right]] = right
    return max(lengths)


def Solution3(s):
    if len(s) < 2:
        return len(s)

    seen = {}
    left = 0
    lengths = {1}

    for right in range(len(s)):
        seen[s[right]] = seen.get(s[right], 0) + 1
        while seen[s[right]] > 1:
            seen[s[left]] -= 1
            left += 1
        lengths.add(right - left + 1)
    return max(lengths)


if __name__ == "__main__":
    cases = [
        ["abcabcbb", 3],
        ["bbbbb", 1],
        ["pwwkew", 3],

        ["", 0],
        ["abcdefghijklmnopqrstuvwxyzabc", 26],
        ["aabcbdeafghijkaabbccddeeffghijklmno", 11],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1, Solution2, Solution3]):
            output = solution(s=deepcopy(case[0]))
            if output != case[1]:
                print(f'Failed   Solution {idx + 1}')
                print(f'Case: {case[0]}, Expected: {case[1]}, Got: {output}')

    print('-' * 150)
    print('Passed all test cases')

