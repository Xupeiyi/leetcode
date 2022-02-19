class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [-1, -1, 0]
        for n in nums:
            count[n] += 1
        # count[2] += count[0] + count[1]
        count[1] += (count[0]+1)
        
        for i in range(len(nums)):
            if i <= count[0]:
                nums[i] = 0
            elif count[0] < i <= count[1]:
                nums[i] = 1
            else:
                nums[i] = 2
    
    
if __name__ == '__main__':
    s = Solution()
    ns = [1, 2, 1, 2, 0, 1, 0]
    s.sortColors(ns)
    print(ns)
    
    
    
    
    

if __name__ == '__main__':
    s = Solution()
    s.sortColors([1, 2, 1, 2, 0, 0])
    