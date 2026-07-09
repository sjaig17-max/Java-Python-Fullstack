"""
1816. Truncate Sentence
https://leetcode.com/problems/truncate-sentence/
"""


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])


if __name__ == "__main__":
    sol = Solution()
    print(sol.truncateSentence("Hello how are you Contestant", 4))  # "Hello how are you"
