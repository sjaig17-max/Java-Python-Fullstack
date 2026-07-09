"""
2108. Find First Palindromic String in the Array
https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
"""
from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""


if __name__ == "__main__":
    sol = Solution()
    print(sol.firstPalindrome(["abc", "car", "ada", "racecar", "cool"]))  # "ada"
