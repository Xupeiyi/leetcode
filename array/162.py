from typing import List
from math import inf

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
            elif nums[mid-1] > nums[mid] > nums[mid+1]:
                end = mid - 1
            elif nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                start = mid + 1
            else:
                break

        return start - 1

if __name__ == '__main__':
    s = Solution()
    ans = s.findPeakElement([3, 2, 1])
    print(ans)