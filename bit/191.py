class Solution:
    def hammingWeight(self, n):
        return sum(1 for i in range(32) if (n >> i) & 1)