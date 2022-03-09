from typing import List
from math import inf

from sortedcontainers import SortedSet

class Solution:
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

if __name__ == '__main__':
    s = Solution()
    ans = s.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3)
    print(ans)

    ans = s.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0)
    print(ans)