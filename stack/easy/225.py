class MyStack:

    def __init__(self):
        self.push_q = [] # 用于输入元素
        self.pop_q = []  # 用于输出元素
    
    @staticmethod
    def transfer(q1, q2):
        # 将q1中元素转移进q2
        while q1:
            element = q1.pop(-1)
            q2.append(element)


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.transfer(self.pop_q, self.push_q)
        self.push_q.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        self.transfer(self.push_q, self.pop_q)
        return self.pop_q.pop(0)


    def top(self) -> int:
        """
        Get the top element.
        """
        if self.push_q:
            return self.push_q[-1]
        if self.pop_q:
            return self.pop_q[0]
        return None
         
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return (self.push_q == []) and (self.pop_q == []) 

if __name__ == '__main__':
    s = MyStack()
    s.push(1)
    s.push(2)
    print(s.top())
    print(s.pop())
    print(s.empty())

