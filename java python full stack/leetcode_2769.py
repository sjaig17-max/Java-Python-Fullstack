"""
2769. Find the Maximum Achievable Number
https://leetcode.com/problems/find-the-maximum-achievable-number/
"""


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t


if __name__ == "__main__":
    sol = Solution()
    print(sol.theMaximumAchievableX(4, 1))  # 6
    print(sol.theMaximumAchievableX(3, 2))  # 7
