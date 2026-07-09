"""
2710. Remove Trailing Zeros From a String
https://leetcode.com/problems/remove-trailing-zeros-from-a-string/
"""


class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip("0")


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeTrailingZeros("51230100"))  # "512301"
