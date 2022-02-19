
def partition(nums, start, end):
    pivot = nums[end]
    
    # [i, j-1] 区间内永远是大于pivot的值
    i = start
    for j in range(start, end):
        if nums[j] > pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    
    nums[i], nums[end] = nums[end], nums[i]
    return i
    

def binFindKthLargest(nums, k, start, end):
    quantile = partition(nums, start, end)
    if quantile > k:
        return binFindKthLargest(nums, k, start, quantile - 1)
    elif quantile < k:
        return binFindKthLargest(nums, k, quantile + 1, end)
    else:
        return nums[quantile]
    

class Solution:
    def findKthLargest(self, nums, k):
        return binFindKthLargest(nums, k-1, 0, len(nums)-1)
        
    
if __name__ == '__main__':
    s = Solution()
    arr = [3,2,1,5,6,4]
    print(arr)
    print(s.findKthLargest(arr, 2))