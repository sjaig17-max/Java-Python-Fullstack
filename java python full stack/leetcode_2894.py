"""
2894. Divisible and Non-divisible Sums Difference
https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
"""


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0  # not divisible by m
        num2 = 0  # divisible by m
        for i in range(1, n + 1):
            if i % m == 0:
                num2 += i
            else:
                num1 += i
        return num1 - num2


if __name__ == "__main__":
    sol = Solution()
    print(sol.differenceOfSums(10, 3))  # 19
    print(sol.differenceOfSums(5, 6))   # 15
