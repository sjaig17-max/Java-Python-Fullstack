"""
234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values == values[::-1]


def build_list(values):
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(build_list([1, 2, 2, 1])))  # True
    print(sol.isPalindrome(build_list([1, 2])))         # False
