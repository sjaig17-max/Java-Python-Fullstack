"""
225. Implement Stack using Queues
https://leetcode.com/problems/implement-stack-using-queues/
"""
from collections import deque


class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        # Rotate the queue so the newly pushed element is at the front,
        # simulating LIFO (stack) order.
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


if __name__ == "__main__":
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(stack.top())    # 2
    print(stack.pop())    # 2
    print(stack.empty())  # False
