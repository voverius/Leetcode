
from Tools.PrintPointers import *


"""
Find the Index of the First Occurrence in a String - MEDIUM
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Given two strings needle and haystack, return the index of the first occurrence of needle in 
haystack, or -1 if needle is not part of haystack.


Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:
1 <= haystack.length, needle.length <= 10^4
haystack and needle consist of only lowercase English characters.
"""


def Solution1(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i] == needle[0] and haystack[i:i + len(needle)] == needle:
            return i
    return -1


if __name__ == "__main__":
    cases = [
        ["sadbutsad", "sad", 0],
        ["leetcode", "leeto", -1],
        ["mississippi", "issip", 4],
        ["abc", "c", 2],

        ["aaaaa", "bba", -1],
        ["a", "a", 0],
        ["hello", "ll", 2],
    ]

    for case in cases:
        for idx, solution in enumerate([Solution1]):
            output = solution(deepcopy(case[0]), deepcopy(case[1]))
            if output != case[2]:
                print(f'Failed   Solution {idx + 1}')
                print(f'Case: haystack={case[0]}, needle={case[1]}, Expected: {case[2]}, Got: {output}')

    print('-' * 150)
    print('Passed all test cases')









