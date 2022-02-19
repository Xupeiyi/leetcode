from typing import List


def next_diff_value(arr, idx):
    i = idx + 1
    while i < len(arr):
        if arr[i] != arr[idx]:
            break
        i += 1
    return i
    

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        i = 0
        j = 0
        while j < len(nums):
            nums[i] = nums[j]
            
            if i > 0 and nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1
            
            if count == 2:
                j = next_diff_value(nums, j)
            else:
                j += 1
            
            i += 1
                 
        return i


## solution 2: 巧用数组已被排序的特点
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        i = 2
        j = 2
        while j < n:
            
            if nums[j] != nums[i-2]: 
                nums[i] = nums[j]
                i += 1

            # 如果nums[j] == nums[i-2], 则nums[i-2], nums[i-1]必是相同的数
            # 继续遍历直到找到不同的数
            j += 1
        return i


if __name__ == '__main__':
    s = Solution()
    l = [1, 1, 2, 2, 2, 3, 3, 4]
    ans = s.removeDuplicates(l)
    print(ans == 7)
    print(l)


    l = [1, 1, 1, 3, 4, 4, 4]
    ans = s.removeDuplicates(l)
    print(ans == 5)
    print(l)

    l = [0,0,1,1,1,1,2,3,3]
    ans = s.removeDuplicates(l)
    print(ans == 7)
    print(l)