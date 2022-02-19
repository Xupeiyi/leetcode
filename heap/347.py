###############################################################
from collections import Counter

def partition(nums, start, end, key):
    pivot = nums[end]
    # [i, j-1] 区间内永远是小于pivot的值
    i = start
    for j in range(start, end):
        if key(nums[j]) > key(pivot):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    
    nums[i], nums[end] = nums[end], nums[i]
    return i


def binSortKthLargest(nums, k, start, end):
    quantile = partition(nums, start, end, key=lambda x: x[1])
    if quantile > k:
        binSortKthLargest(nums, k, start, quantile-1)
    if quantile > k:
        return binSortKthLargest(nums, k, start, quantile - 1)
    elif quantile < k:
        return binSortKthLargest(nums, k, quantile + 1, end)


class Solution1:
    def topKFrequent(self, nums, k: int):
        count = Counter(nums)
        count_list = [(num, freq) for num, freq in count.items()]
        binSortKthLargest(count_list, k-1, 0, len(count_list)-1)
        return [c[0] for c in count_list[:k]]
        
        
#######################################################
from queue import PriorityQueue

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        q = PriorityQueue(k)
        for num, freq in count.items():
            if q.full():
                head_freq, head_num = q.get()
                if head_freq > freq:
                    q.put([head_freq, head_num])
                else:
                    q.put([freq, num])
            else:
                q.put([freq, num])
        
        return [q.get()[1] for _ in range(k)]



if __name__ == '__main__':
    s = Solution()
    ans = s.topKFrequent([5, 3, 1, 1, 1, 3, 73, 1], 2)
    print(ans)