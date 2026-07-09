"""
657. Robot Return to Origin
https://leetcode.com/problems/robot-return-to-origin/
"""


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = moves.count("R") - moves.count("L")
        y = moves.count("U") - moves.count("D")
        return x == 0 and y == 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.judgeCircle("UD"))    # True
    print(sol.judgeCircle("LL"))    # False
