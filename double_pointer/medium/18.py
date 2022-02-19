def skip_same_value(nums, idx, direction):
    """返回下一个与nums[pos]不同值的位置"""
    original_value = nums[idx]
    while True:
        idx += direction
        if idx >= len(nums) or idx < 0 or nums[idx] != original_value:
            break
    return idx


def twoSum(nums, target, start):
    ans = []
    end = len(nums) - 1
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
    

def threeSum(nums, target, start):
    nums = sorted(nums)
    ans = []

    while start <= len(nums)-3:
        if nums[start] > 0 and nums[start] > target:
            break
        pairs = twoSum(nums, target-nums[start], start+1)
        if pairs:
            ans += [[nums[start], pair[0], pair[1]] for pair in pairs]
        start = skip_same_value(nums, start, 1)
        
    return ans


class Solution:
    def fourSum(self, nums, target):
        nums = sorted(nums)
        ans = []
        start = 0
        while start <= len(nums)-4:
            if nums[start] > 0 and nums[start] > target:
                break
            triples = threeSum(nums, target-nums[start], start+1)
            if triples:
                ans += [[nums[start]] + triple for triple in triples]
            start = skip_same_value(nums, start, 1)
        return ans
        
        
if __name__ == '__main__':
    s = Solution()
    arr = [-5, -4, -3, -2, 1, 3, 3, 5]
    a = s.fourSum(arr, -11)
    print(a)