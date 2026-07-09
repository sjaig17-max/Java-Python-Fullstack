"""
1672. Richest Customer Wealth
https://leetcode.com/problems/richest-customer-wealth/
"""
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(account) for account in accounts)


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumWealth([[1, 2, 3], [3, 2, 1]]))  # 6
    print(sol.maximumWealth([[1, 5], [7, 3], [3, 5]]))  # 10
