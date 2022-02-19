class Empty(Exception):
    pass

class Stack:

    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def empty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)
    
    def top(self):
        if self.empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        if self.empty():
            raise Empty('Stack is empty')
        return self._data.pop()

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack = Stack()
        self.pop_stack = Stack()

    @staticmethod
    def transfer(stack1, stack2):
        while stack1:
            e = stack1.pop()
            stack2.push(e)

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.push_stack.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """ 
        if not self.pop_stack:
            self.transfer(self.push_stack, self.pop_stack)
        if not self.pop_stack:
            return None
        return self.pop_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.pop_stack:
            self.transfer(self.push_stack, self.pop_stack)
        if not self.pop_stack:
            return None
        return self.pop_stack.top()

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.push_stack.empty() and self.pop_stack.empty()

if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.pop()) # 1
    print(q.pop()) # 2
    q.push(4)
    print(q.peek()) # 3
