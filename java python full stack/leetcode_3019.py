"""
3019. Number of Changing Keys
https://leetcode.com/problems/number-of-changing-keys/
"""


class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes


if __name__ == "__main__":
    sol = Solution()
    print(sol.countKeyChanges("aAbBcC"))  # 2
