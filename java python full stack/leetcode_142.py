"""
142. Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                pointer = head
                while pointer != slow:
                    pointer = pointer.next
                    slow = slow.next
                return pointer
        return None


if __name__ == "__main__":
    # Build a list with a cycle: 3 -> 2 -> 0 -> -4 -> back to node with value 2
    n3 = ListNode(3)
    n2 = ListNode(2)
    n0 = ListNode(0)
    n4 = ListNode(-4)
    n3.next, n2.next, n0.next, n4.next = n2, n0, n4, n2

    sol = Solution()
    result = sol.detectCycle(n3)
    print(result.val if result else None)  # 2
