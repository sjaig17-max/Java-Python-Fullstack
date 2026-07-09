"""
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    n3 = ListNode(3)
    n2 = ListNode(2)
    n0 = ListNode(0)
    n4 = ListNode(-4)
    n3.next, n2.next, n0.next, n4.next = n2, n0, n4, n2

    sol = Solution()
    print(sol.hasCycle(n3))  # True

    n1 = ListNode(1)
    n1.next = None
    print(sol.hasCycle(n1))  # False
