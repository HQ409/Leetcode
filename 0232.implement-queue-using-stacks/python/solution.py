# -*- coding: utf-8 -*-

class MyQueue:
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []
        self._peek = None

    def push(self, x: int) -> None:
        self.push_stack.append(x)
        if len(self.push_stack) == 1:
            self._peek = x

    def pop(self) -> int:
        if len(self.pop_stack) > 0:
            return self.pop_stack.pop()
        while len(self.push_stack) > 1:
            self.pop_stack.append(self.push_stack.pop())
        return self.push_stack.pop()

    def peek(self) -> int:
        if len(self.pop_stack) > 0:
            return self.pop_stack[-1]
        return self._peek

    def empty(self) -> bool:
        return len(self.push_stack) + len(self.pop_stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()