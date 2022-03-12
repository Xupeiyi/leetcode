from typing import List

# 此题与238极为相似，只是238不允许使用除法。
# 如何找出不存在的个体？将f(整体)与f(除去个体)进行对比。
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n+1) * n // 2 - sum(nums)
