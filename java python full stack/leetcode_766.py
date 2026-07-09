"""
766. Toeplitz Matrix
https://leetcode.com/problems/toeplitz-matrix/
"""
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows - 1):
            for c in range(cols - 1):
                if matrix[r][c] != matrix[r + 1][c + 1]:
                    return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))  # True
