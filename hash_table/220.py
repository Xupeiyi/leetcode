from typing import List
from math import inf

from sortedcontainers import SortedSet

class Solution1:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        window = SortedSet([-inf, inf])  # 最好使用ordered set, 但python 标准库不支持
        
        for i, num in enumerate(nums):
            idx = window.bisect_left(num)
            if num - window[idx-1] <= t or window[idx] - num <= t:
                return True
            window.add(num)  # 频繁加入和弹出元素可能导致列表元素被频繁移动而导致低效 
                             # (但leetcode执行结果表示差别不太大)
            if i >= k:
                # pop_idx = bisect.bisect_left(window, nums[i-k])
                window.discard(nums[i-k])  
            
        return False


# 桶排序
class Solution:

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        size = t + 1
        def bucket_idx(n):
            nonlocal size
            return (n + 1) // size - 1 if n < 0 else n // size
        
        buckets = dict()
        for i, num in enumerate(nums):
            idx = bucket_idx(num)
            if idx in buckets:
                return True
            
            for adj_idx in [idx-1, idx+1]:
                if adj_idx in buckets and abs(num - buckets[adj_idx]) <= t:
                    return True
            buckets[idx] = num

            if i >= k:
                buckets.pop(bucket_idx(nums[i-k]))
        
        return False


if __name__ == '__main__':
    s = Solution()
    ans = s.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3)
    print(ans)

    ans = s.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0)
    print(ans)