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
    

class Solution1:
    
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        return binSearchRange(nums, target, 0, len(nums)-1)


# 另一种做法：分两次查找， 一次查找最左边的索引， 另一次查找最右边的索引
def bisect_leftmost(nums, target):
    start, end = 0, len(nums)-1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] < target:
            start = mid + 1
        # 因为要查找最左边的值，所以当nums[mid] == target时也向左查找
        # 此时有两种情况：1. nums[end] == target， 则此情形与之前相同
        #                2. nums[end] < target， 则start逐渐增大至start = end + 1, 然后停止循环
        else:
            end = mid - 1
    return start if start < len(nums) and nums[start] == target else -1

# bisect_rightmost与bisect_leftmost完全对称
def bisect_rightmost(nums, target):
    start, end = 0, len(nums)-1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return end if end >= 0 and nums[end] == target else -1

class Solution:
    
    def searchRange(self, nums, target):
        left_idx = bisect_leftmost(nums, target)
        right_idx = bisect_rightmost(nums, target)
        return [left_idx, right_idx]
    
if __name__ == '__main__':
    s = Solution()
    ans = s.searchRange([1, 2, 8, 8, 8], 8)
    print(ans)
    