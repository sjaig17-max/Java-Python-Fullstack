"""
2574. Left and Right Sum Differences
https://leetcode.com/problems/left-and-right-sum-differences/
"""
from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = [0] * n
        right_sum = [0] * n

        running = 0
        for i in range(n):
            left_sum[i] = running
            running += nums[i]

        running = 0
        for i in range(n - 1, -1, -1):
            right_sum[i] = running
            running += nums[i]

        return [abs(left_sum[i] - right_sum[i]) for i in range(n)]


if __name__ == "__main__":
    sol = Solution()
    print(sol.leftRightDifference([10, 4, 8, 3]))  # [15, 1, 11, 22]
