"""
520. Detect Capital
https://leetcode.com/problems/detect-capital/
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()


if __name__ == "__main__":
    sol = Solution()
    print(sol.detectCapitalUse("USA"))    # True
    print(sol.detectCapitalUse("FlaG"))   # False
