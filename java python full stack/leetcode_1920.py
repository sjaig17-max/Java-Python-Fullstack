"""
1920. Build Array from Permutation
https://leetcode.com/problems/build-array-from-permutation/
"""
from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]


if __name__ == "__main__":
    sol = Solution()
    print(sol.buildArray([0, 2, 1, 5, 3, 4]))  # [0, 1, 2, 4, 5, 3]
