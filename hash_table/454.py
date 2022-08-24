from typing import List
from collections import Counter


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        sum1 = {n1 + n2: c1 * c2 for n1, c1 in count1.items() for n2, c2 in count2.items()}
        
        count3 = Counter(nums3)
        count4 = Counter(nums4)
        sum2 = {n3 + n4: c3 * c4 for n3, c3 in count3.items() for n4, c4 in count4.items()}

        ans = 0
        for s1, n1 in sum1.items():
            ans += n1 * sum2.get(-s1, 0)
        return ans 
