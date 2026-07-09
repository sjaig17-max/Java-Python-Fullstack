"""
2022. Convert 1D Array Into 2D Array
https://leetcode.com/problems/convert-1d-array-into-2d-array/
"""
from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        return [original[i * n:(i + 1) * n] for i in range(m)]


if __name__ == "__main__":
    sol = Solution()
    print(sol.construct2DArray([1, 2, 3, 4], 2, 2))
    print(sol.construct2DArray([1, 2, 3], 1, 3))
