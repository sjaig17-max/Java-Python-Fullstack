"""
2652. Sum Multiples
https://leetcode.com/problems/sum-multiples/
"""


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum(i for i in range(1, n + 1) if i % 3 == 0 or i % 5 == 0 or i % 7 == 0)


if __name__ == "__main__":
    sol = Solution()
    print(sol.sumOfMultiples(7))   # 21
    print(sol.sumOfMultiples(10))  # 40
