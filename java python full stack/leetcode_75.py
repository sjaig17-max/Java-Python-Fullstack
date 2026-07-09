"""
75. Sort Colors
https://leetcode.com/problems/sort-colors/
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Dutch National Flag algorithm.
        """
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 0, 2, 1, 1, 0]
    sol.sortColors(arr)
    print(arr)  # [0, 0, 1, 1, 2, 2]
