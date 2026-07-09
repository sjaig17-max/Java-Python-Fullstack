"""
1046. Last Stone Weight
https://leetcode.com/problems/last-stone-weight/
"""
import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Use negative values to simulate a max-heap with heapq (a min-heap).
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            if first != second:
                heapq.heappush(heap, -(first - second))

        return -heap[0] if heap else 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.lastStoneWeight([2, 7, 4, 1, 8, 1]))  # 1
