from typing import List

# 前缀和
# 不要看到求序列的开始和结束就想到二维数组
# 当求最优的规则发生变化时， 分两次解决
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        decrease, increase = [0] * n, [0] * n
        for i in range(1, n):
            if security[i] <= security[i-1]:
                decrease[i] = decrease[i-1] + 1
            if security[n-i-1] <= security[n-i]:
                increase[n-i-1] = increase[n-i] + 1
        
        return [i for i in range(time, n-time) if decrease[i] >= time and increase[i] >= time]