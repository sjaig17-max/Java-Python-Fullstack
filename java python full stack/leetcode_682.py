"""
682. Baseball Game
https://leetcode.com/problems/baseball-game/
"""
from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)


if __name__ == "__main__":
    sol = Solution()
    print(sol.calPoints(["5", "2", "C", "D", "+"]))  # 30
    print(sol.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))  # 27
