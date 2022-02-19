
def skip_same_value(nums, idx, direction):
    """返回下一个与nums[pos]不同值的位置"""
    original_value = nums[idx]
    while True:
        idx += direction
        if idx >= len(nums) or idx < 0 or nums[idx] != original_value:
            break
    return idx


def find_target_sum(nums, target, start, end):
    ans = []
    while start < end:
        sum_ = nums[start] + nums[end]
        if sum_ > target:
            end = skip_same_value(nums, end, -1)
        elif sum_ < target:
            start = skip_same_value(nums, start, 1)
        else:
            ans.append([nums[start], nums[end]])
            start = skip_same_value(nums, start, 1)
            end = skip_same_value(nums, end, -1)
    return ans
    

class Solution:
    def threeSum(self, nums):
        length = len(nums)
        if length < 3:
            return []
        
        nums = sorted(nums)
        ans = []
        i = 0
        while i <= length-3:
            if nums[i] > 0:
                break
            pairs = find_target_sum(nums, -nums[i], i+1, length-1)
            if pairs:
                ans += [[nums[i], pair[0], pair[1]] for pair in pairs]
            i = skip_same_value(nums, i, 1)
            
        return ans
        
        
if __name__ == '__main__':
    s = Solution()
    arr = [0, 0, 0]
    a = s.threeSum(arr)
    print(a)