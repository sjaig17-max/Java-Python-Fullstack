"""
1295. Find Numbers with Even Number of Digits
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
"""
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for num in nums if len(str(num)) % 2 == 0)


if __name__ == "__main__":
    sol = Solution()
    print(sol.findNumbers([12, 345, 2, 6, 7896]))  # 2
