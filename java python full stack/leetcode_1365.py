"""
1365. How Many Numbers Are Smaller Than the Current Number
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
"""
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        rank = {}
        for i, num in enumerate(sorted_nums):
            if num not in rank:
                rank[num] = i
        return [rank[num] for num in nums]


if __name__ == "__main__":
    sol = Solution()
    print(sol.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))  # [4, 0, 1, 1, 3]
