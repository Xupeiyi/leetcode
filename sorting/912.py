from typing import List
from random import shuffle

def partition(nums, lo, hi):
    pivot = nums[lo]
    i = lo + 1  # nums[low+1, i-1] <= pivot
    j = hi  # nums[j+1, hi] > pivot
    
    while i <= j:
        while i < hi and nums[i] <= pivot:
            i += 1
        while j > lo and nums[j] > pivot:
            j -= 1

        if i >= j:
            break

        nums[i], nums[j] = nums[j], nums[i]
    nums[lo], nums[j] = nums[j], nums[lo]
    return j

def sort(nums, lo, hi):
    if lo >= hi:
        return
    
    k = partition(nums, lo, hi)
    sort(nums, lo, k-1)
    sort(nums, k+1, hi)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        shuffle(nums)
        sort(nums, 0, len(nums)-1)
        return nums


if __name__ == '__main__':
    ans = partition([4, 2, 3, 1, 5, 7, 6], 0, 6)
    print(ans)

    s = Solution()
    ans = s.sortArray([5,1,1,2,0,0])
    print(ans)

