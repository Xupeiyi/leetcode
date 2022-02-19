class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        max_length = 1
        curr_length = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr_length += 1
            else:
                if curr_length > max_length:
                    max_length = curr_length
                curr_length = 1
        return max(max_length, curr_length)