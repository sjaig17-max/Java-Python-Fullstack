"""
1351. Count Negative Numbers in a Sorted Matrix
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
"""
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        n_cols = len(grid[0])
        col = n_cols - 1
        for row in grid:
            while col >= 0 and row[col] < 0:
                col -= 1
            count += n_cols - 1 - col
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))  # 8
