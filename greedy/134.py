class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        gains = [gas[i]-cost[i] for i in range(len(gas))]
        if sum(gains) < 0:
            return -1
        
        sum_ = 0
        ans = 0
        for i, gain in enumerate(gains):
            if sum_ + gain < 0:
                ans = i + 1
                sum_ = 0
            else:
                sum_ += gain
        return ans


if __name__ == '__main__':
    s = Solution()
    ans = s.canCompleteCircuit([3, 1, 1], [1, 2, 2])
    print(ans)
        
        
        