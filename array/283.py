class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length <= 1:
            return
        
        i = 0
        for j in range(0, length):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        for k in range(i, length):
            nums[k] = 0

if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    print(nums)