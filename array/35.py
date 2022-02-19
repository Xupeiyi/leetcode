def binInsert(nums, start, end, target):
    if start >= end:
        if target <= nums[start]:
            return start
        else:
            return start + 1
    mid = (start + end) // 2
    if target < nums[mid]:
        return binInsert(nums, start, mid-1, target)
    elif target > nums[mid]:
        return binInsert(nums, mid+1, end, target)
    else:
        return mid
        
        
class Solution:
    def searchInsert(self, nums, target):
        return binInsert(nums, 0, len(nums)-1, target)
    

if __name__ == '__main__':
    s = Solution()
    ans = s.searchInsert([1, 3], 0)  # 如果写 if start == end 则报错
    print(ans)