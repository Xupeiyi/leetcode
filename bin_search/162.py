from typing import List
from math import inf

# 如何看出本题可以用二分查找：mid左右两边不同
# 可以推测，target一定能出现在具备上升路径的那一边。
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-inf] + nums + [-inf] 
        start, end = 1, len(nums) - 2

        while start < end:
            mid = (start + end) // 2

            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid - 1
            elif nums[mid-1] < nums[mid] < nums[mid+1]:
                start = mid + 1
            # 如果mid是谷值，则在哪一边查找都可以
            else:
                end = mid - 1

        return start - 1


if __name__ == '__main__':
    s = Solution()
    ans = s.findPeakElement([3, 2, 1])
    print(ans)