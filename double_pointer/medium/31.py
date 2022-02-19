class Solution1:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        
        swap_idx = len(nums) - 2
        # find the number to be swap behind
        for i in range(len(nums)-2, -1, -1):
            swap_idx = i
            if nums[i] < nums[i+1]:
                break
        
        # find the minimum number that is larger than the swap number

        put_before = len(nums) - 1
        for i in range(len(nums)-1, swap_idx-1, -1):
            put_before = i
            if nums[i] > nums[swap_idx]:
                break
        
        if swap_idx == put_before:
            swap_idx -= 1
            put_before -= 1
        
        # put nums[put_before:] before nums[swap_idx]
        # 1.
        nums[swap_idx], nums[put_before] = nums[put_before], nums[swap_idx]
        
        # 2.
        i, j = swap_idx + 1, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


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
    nums = [3, 2, 1]
    s.nextPermutation(nums)
    print(nums)
        
        
            
        
        
        