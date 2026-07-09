"""
2239. Find Closest Number to Zero
https://leetcode.com/problems/find-closest-number-to-zero/
"""
from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        best = nums[0]
        for num in nums[1:]:
            if abs(num) < abs(best) or (abs(num) == abs(best) and num > best):
                best = num
        return best


if __name__ == "__main__":
    sol = Solution()
    print(sol.findClosestNumber([-4, -2, 1, 4, 8]))  # 1
