"""
2678. Number of Senior Citizens
https://leetcode.com/problems/number-of-senior-citizens/
"""
from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(1 for d in details if int(d[11:13]) > 60)


if __name__ == "__main__":
    sol = Solution()
    print(sol.countSeniors(["7868190130M7522", "5303914400F9211", "9273338290F4010"]))  # 2
