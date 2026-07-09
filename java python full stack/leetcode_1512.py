"""
1512. Number of Good Pairs
https://leetcode.com/problems/number-of-good-pairs/
"""
from typing import List
from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = defaultdict(int)
        good_pairs = 0
        for num in nums:
            good_pairs += count[num]
            count[num] += 1
        return good_pairs


if __name__ == "__main__":
    sol = Solution()
    print(sol.numIdenticalPairs([1, 2, 3, 1, 1, 3]))  # 4
