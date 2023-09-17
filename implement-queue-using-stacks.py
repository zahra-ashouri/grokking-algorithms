"""
https://leetcode.com/problems/implement-queue-using-stacks/

main idea: one stack to read, and the other to write

"""


class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        if not self.stack1:
            return None
        return self.stack1.pop()

    def peek(self) -> int:
        if not self.stack1:
            return None
        return self.stack1[-1]

    def empty(self) -> bool:
        return False if self.stack1 else True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()