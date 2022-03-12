from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1, c1 = 0, 0
        cnt2, c2 = 0, 0

        for n in nums:
            if n == c1 and cnt1 > 0:
                cnt1 += 1
            
            elif n == c2 and cnt2 > 0:
                cnt2 += 1

            elif cnt1 == 0:
                c1 = n
                cnt1 += 1
            
            elif cnt2 == 0:
                c2 = n
                cnt2 += 1

            else:
                cnt1 -= 1
                cnt2 -= 1
            
        n1, n2 = 0, 0
        for num in nums:
            if cnt1 > 0 and num == c1:
                n1 += 1
            if cnt2 > 0 and num == c2:
                n2 += 1

        ans = []
        if cnt1 > 0 and n1 > len(nums) // 3:
            ans.append(c1)
        if cnt2 > 0 and n2 > len(nums) // 3:
            ans.append(c2)
        return ans