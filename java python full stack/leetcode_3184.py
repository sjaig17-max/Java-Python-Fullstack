"""
3184. Count Pairs That Form a Complete Day I
https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/
"""
from typing import List
from collections import defaultdict


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        remainder_count = defaultdict(int)
        count = 0
        for h in hours:
            r = h % 24
            complement = (24 - r) % 24
            count += remainder_count[complement]
            remainder_count[r] += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.countCompleteDayPairs([12, 12, 30, 24, 24]))  # 2
    print(sol.countCompleteDayPairs([72, 48, 24, 3]))       # 3
