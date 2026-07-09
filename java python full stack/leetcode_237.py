"""
237. Delete Node in a Linked List
https://leetcode.com/problems/delete-node-in-a-linked-list/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        node.val = node.next.val
        node.next = node.next.next


if __name__ == "__main__":
    # Build 4 -> 5 -> 1 -> 9
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1 = ListNode(1)
    n9 = ListNode(9)
    n4.next, n5.next, n1.next = n5, n1, n9

    sol = Solution()
    sol.deleteNode(n5)  # delete node with value 5

    values = []
    cur = n4
    while cur:
        values.append(cur.val)
        cur = cur.next
    print(values)  # [4, 1, 9]
