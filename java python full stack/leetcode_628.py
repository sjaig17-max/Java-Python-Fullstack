"""
628. Maximum Product of Three Numbers
https://leetcode.com/problems/maximum-product-of-three-numbers/
"""
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        # Either the three largest numbers, or the two smallest (most negative)
        # combined with the largest number.
        return max(
            nums[-1] * nums[-2] * nums[-3],
            nums[0] * nums[1] * nums[-1]
        )


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumProduct([1, 2, 3]))        # 6
    print(sol.maximumProduct([1, 2, 3, 4]))     # 24
    print(sol.maximumProduct([-1, -2, -3]))     # -6
