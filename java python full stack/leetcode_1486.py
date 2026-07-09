"""
1486. XOR Operation in an Array
https://leetcode.com/problems/xor-operation-in-an-array/
"""
from typing import List


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for i in range(n):
            result ^= (start + 2 * i)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.xorOperation(5, 0))   # 8
    print(sol.xorOperation(4, 3))   # 8
