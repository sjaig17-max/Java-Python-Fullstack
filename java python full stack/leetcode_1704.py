"""
1704. Determine if String Halves Are Alike
https://leetcode.com/problems/determine-if-string-halves-are-alike/
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        mid = len(s) // 2
        first_half_count = sum(1 for c in s[:mid] if c in vowels)
        second_half_count = sum(1 for c in s[mid:] if c in vowels)
        return first_half_count == second_half_count


if __name__ == "__main__":
    sol = Solution()
    print(sol.halvesAreAlike("book"))  # True
    print(sol.halvesAreAlike("textbook"))  # False
