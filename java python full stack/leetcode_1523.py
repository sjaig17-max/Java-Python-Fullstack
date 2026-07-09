"""
1523. Count Odd Numbers in an Interval Range
https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total = high - low + 1
        if low % 2 == 1 or high % 2 == 1:
            return (total + 1) // 2
        return total // 2


if __name__ == "__main__":
    sol = Solution()
    print(sol.countOdds(3, 7))  # 3
    print(sol.countOdds(8, 10))  # 1
