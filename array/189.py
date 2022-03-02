from typing import List

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n 
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)

if __name__ == '__main__':
    s = Solution()
    a = [1, 2, 3, 4, 5]
    s.rotate(a, 6)
    print(a)