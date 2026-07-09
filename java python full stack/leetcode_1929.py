"""
1929. Concatenation of Array
https://leetcode.com/problems/concatenation-of-array/
"""
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


if __name__ == "__main__":
    sol = Solution()
    print(sol.getConcatenation([1, 2, 1]))  # [1, 2, 1, 1, 2, 1]
