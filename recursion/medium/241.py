from typing import List
from operator import add, sub, mul

funcs = {
    "+": add,
    "-": sub,
    "*": mul
}

# 简洁的分治。不知道为啥有的题解写得那么复杂...
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isnumeric():
            return [int(expression)]
        
        results = []
        for i, char in enumerate(expression[1:-1], start=1):
            if char in ("+-*/"):
                results += [funcs[char](n1, n2) 
                            for n1 in self.diffWaysToCompute(expression[:i]) 
                            for n2 in self.diffWaysToCompute(expression[i+1:])]
        
        return results

if __name__ == '__main__':
    s = Solution()
    ans = s.diffWaysToCompute("2*3-4*5")
    print(ans)