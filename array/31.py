class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # find the number to be swapped
        # the number to be swapped is the number from which a sorted order is breached
        # when iterating from the end
        i = len(nums) - 2
        while nums[i] >= nums[i + 1] and i >= 0:
            i -= 1
        
        # if nums is not sorted in a reversed order,
        # find a number from nums[i+1:] to swap together with nums[i]
        # the number is the first one that is larger than nums[i], as
        # nums[i+1:] is sorted in reversed order
        if i > -1:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # reverse nums[i+1:] to get a sorted order
        start = i + 1
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 5, 1]
    s.nextPermutation(nums)
    print(nums)
