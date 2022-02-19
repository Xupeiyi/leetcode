def binSearchRange(nums, target, start, end):
    if start >= end:
        return [start, start] if nums[start] == target else [-1, -1]

    mid = (start + end) // 2
    if nums[mid] > target:
        return binSearchRange(nums, target, start, mid - 1)
    elif nums[mid] < target:
        return binSearchRange(nums, target, mid+1, end)
    else:
        t_start = binSearchRange(nums, target, start, mid - 1)[0]
        t_start = mid if t_start == -1 else t_start
        t_end = binSearchRange(nums, target, mid + 1, end)[1]
        t_end = mid if t_end == -1 else t_end
        return [t_start, t_end]
    
    # l_start, l_end = binSearchRange(nums, target, start, mid)
    # r_start, r_end = binSearchRange(nums, target, mid+1, end)
    # start = l_start if l_start != -1 else r_start
    # end = r_end if r_end != -1 else l_end
    # return [start, end]
    
    

class Solution:
    
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        return binSearchRange(nums, target, 0, len(nums)-1)
    
    
if __name__ == '__main__':
    s = Solution()
    ans = s.searchRange([1, 2, 8, 8, 8], 8)
    print(ans)
    