"""
2006. Count Number of Pairs With Absolute Difference K
https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
"""
from typing import List
from collections import defaultdict


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        seen = defaultdict(int)
        for num in nums:
            count += seen[num - k] + seen[num + k]
            seen[num] += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.countKDifference([1, 2, 2, 1], 1))  # 4
