"""
1480. Running Sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array/
"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        total = 0
        for num in nums:
            total += num
            result.append(total)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.runningSum([1, 2, 3, 4]))     # [1, 3, 6, 10]
    print(sol.runningSum([1, 1, 1, 1, 1]))  # [1, 2, 3, 4, 5]
