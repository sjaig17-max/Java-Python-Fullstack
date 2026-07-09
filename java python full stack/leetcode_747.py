"""
747. Largest Number At Least Twice of Others
https://leetcode.com/problems/largest-number-at-least-twice-of-others/
"""
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_idx = 0
        for i, num in enumerate(nums):
            if num > nums[max_idx]:
                max_idx = i

        for i, num in enumerate(nums):
            if i != max_idx and nums[max_idx] < 2 * num:
                return -1
        return max_idx


if __name__ == "__main__":
    sol = Solution()
    print(sol.dominantIndex([3, 6, 1, 0]))  # 1
    print(sol.dominantIndex([1, 2, 3, 4]))  # -1
