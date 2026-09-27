
## My soltuion:
from collections import deque

class MyStack:

    def __init__(self):
        self.up_queue = deque()
        self.down_queue = deque()

    def push(self, x: int) -> None:
        if len(self.up_queue) == 0:
            self.up_queue.append(x)
        else:
            while len(self.up_queue) > 0:
                self.down_queue.append(self.up_queue.popleft())
            self.up_queue.append(x)
            while len(self.down_queue) > 0:
                self.up_queue.append(self.down_queue.popleft())
        

    def pop(self) -> int:
        if len(self.up_queue) > 0:
            return self.up_queue.popleft()

    def top(self) -> int:
        return self.up_queue[0]

    def empty(self) -> bool:
        return len(self.up_queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()