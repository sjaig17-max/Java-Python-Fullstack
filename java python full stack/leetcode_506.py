"""
506. Relative Ranks
https://leetcode.com/problems/relative-ranks/
"""
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        indexed = sorted(range(n), key=lambda i: score[i], reverse=True)
        result = [""] * n

        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for rank, idx in enumerate(indexed):
            if rank < 3:
                result[idx] = medals[rank]
            else:
                result[idx] = str(rank + 1)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.findRelativeRanks([5, 4, 3, 2, 1]))
    # ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
