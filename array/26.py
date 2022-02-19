class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) <= 1:
            return nums

        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i += 1 
        return i


if __name__ == '__main__':
    s = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    i = s.removeDuplicates(nums)
    print(nums[:i])