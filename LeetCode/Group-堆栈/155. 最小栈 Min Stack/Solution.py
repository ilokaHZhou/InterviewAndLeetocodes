class MinStack:

    def __init__(self):
        self.stack = [] # 主栈, 用于存值
        self.min_stack = []  # 辅助栈，用于存储最小值
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        # 如果辅助栈为空，或者新元素小于等于辅助栈的栈顶元素，则同时压入辅助栈
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            # 如果弹出的元素等于辅助栈的栈顶元素，则同时弹出辅助栈的栈顶元素
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()