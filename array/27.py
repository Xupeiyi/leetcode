class Solution:
    def removeElement(self, nums, val: int) -> int:
        i, j = 0, 0
        for j in range(0, len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i






if __name__ == '__main__':
    s = Solution()
    nums = [3]
    val = 2
    i = s.removeElement(nums, val)
    print(i)
    print(nums[:i])