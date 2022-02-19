import math

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []
        self.min = [math.inf]


    def push(self, x: int) -> None:
        self.values.append(x)
        self.min.append(min(x, self.min[-1]))

    def pop(self) -> None:
        self.values.pop(-1)
        self.min.pop(-1)

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.min[-1]



# Your MinStack object will be instantiated and called as such:
x = 3
obj = MinStack()
obj.push(x)
obj.push(5)
obj.pop()
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)