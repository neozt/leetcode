class MinStack:

    def __init__(self):
        self.stack = []
        self.current_min = float("inf")


    def push(self, val: int) -> None:
        prev_min = self.current_min
        self.current_min = min(val, prev_min)
        self.stack.append((val, prev_min))

    def pop(self) -> None:
        (_, prev_min) = self.stack.pop(-1)
        self.current_min = prev_min

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.current_min

# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())
min_stack.pop()
print(min_stack.top())
print(min_stack.getMin())
min_stack.pop()
print(min_stack.top())
print(min_stack.getMin())
