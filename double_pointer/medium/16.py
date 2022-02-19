import math


def twoSumClosest(nums, target):
    i, j = 0, len(nums)-1
    
    closest = math.inf
    dist = math.inf
    while i < j:
        curr_sum = nums[i] + nums[j]
        curr_dist = abs(curr_sum - target)
        if curr_dist < dist:
            closest = curr_sum
            dist = curr_dist
        
        if curr_sum == target:
            break
        elif curr_sum > target:
            j -= 1
        elif curr_sum < target:
            i += 1
    return closest


class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        sorted_nums = sorted(nums)
        
        closest = math.inf
        dist = math.inf
        for i, n in enumerate(sorted_nums[:-2]):
            curr_sum = n + twoSumClosest(sorted_nums[i+1:], target-n)
            curr_dist = abs(curr_sum - target)
            if curr_dist < dist:
                closest = curr_sum
                dist = curr_dist
            
            if dist == 0:
                break
        
        return closest
        
        
if __name__ == '__main__':
    s = Solution()
    ans = twoSumClosest([0, 2, 3, 4, 5, 100], 95)
    print(ans)
    
    ans = s.threeSumClosest([-1, 2, 1, 4], 8)
    print(ans)