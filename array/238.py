from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for _ in nums]

        n = len(nums)
        pre_product = nums[0]
        for i in range(1, n):
            ans[i] *= pre_product
            pre_product *= nums[i]
        
        post_product = nums[n-1]
        for i in range(n-2, -1, -1):
            ans[i] *= post_product
            post_product *= nums[i]
        
        return ans