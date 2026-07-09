"""
191. Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n - 1)  # clear the lowest set bit
            count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingWeight(11))          # 3 (1011)
    print(sol.hammingWeight(128))         # 1 (10000000)
