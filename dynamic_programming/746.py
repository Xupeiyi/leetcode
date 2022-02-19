class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        # 跳到这一级总共花费体力
        cost = cost + [0]
        total_cost = [0] * len(cost)
        
        for i in range(2, len(total_cost)):
            total_cost[i] = min(cost[i-2] + total_cost[i-2], cost[i-1] + total_cost[i-1])
        
        return total_cost[-1]
    
    
if __name__ == '__main__':
    s = Solution()
    c = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    ans = s.minCostClimbingStairs(c)
    print(ans)