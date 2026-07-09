"""
231. Power of Two
https://leetcode.com/problems/power-of-two/
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfTwo(1))   # True
    print(sol.isPowerOfTwo(16))  # True
    print(sol.isPowerOfTwo(3))   # False
