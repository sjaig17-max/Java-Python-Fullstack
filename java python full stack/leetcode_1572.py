"""
1572. Matrix Diagonal Sum
https://leetcode.com/problems/matrix-diagonal-sum/
"""
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0
        for i in range(n):
            total += mat[i][i]
            if i != n - 1 - i:
                total += mat[i][n - 1 - i]
        return total


if __name__ == "__main__":
    sol = Solution()
    print(sol.diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # 25
