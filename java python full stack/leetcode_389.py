"""
389. Find the Difference
https://leetcode.com/problems/find-the-difference/
"""
from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_t = Counter(t)
        count_s = Counter(s)
        diff = count_t - count_s
        return next(iter(diff))


if __name__ == "__main__":
    sol = Solution()
    print(sol.findTheDifference("abcd", "abcde"))  # "e"
