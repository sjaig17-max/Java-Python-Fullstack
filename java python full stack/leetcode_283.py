"""
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        for i in range(insert_pos, len(nums)):
            nums[i] = 0


if __name__ == "__main__":
    sol = Solution()
    arr = [0, 1, 0, 3, 12]
    sol.moveZeroes(arr)
    print(arr)  # [1, 3, 12, 0, 0]
