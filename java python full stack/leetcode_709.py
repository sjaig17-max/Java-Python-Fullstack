"""
709. To Lower Case
https://leetcode.com/problems/to-lower-case/
"""


class Solution:
    def toLowerCase(self, s: str) -> str:
        result = []
        for c in s:
            if "A" <= c <= "Z":
                result.append(chr(ord(c) + 32))
            else:
                result.append(c)
        return "".join(result)


if __name__ == "__main__":
    sol = Solution()
    print(sol.toLowerCase("LEETCODE"))  # "leetcode"
