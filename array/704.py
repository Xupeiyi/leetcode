class Solution:

    def binary_search(self, nums, target, low, high):
        if low > high:
            return -1

        mid = (high + low) // 2
        m_value = nums[mid]

        if m_value < target:
            return self.binary_search(nums, target, mid+1, high)
        elif m_value > target:
            return self.binary_search(nums, target, low, mid-1)
        else:
            return mid



    def search(self, nums, target: int) -> int:
        return self.binary_search(nums, target, low=0, high=len(nums)-1)
        


if __name__ == '__main__':
    s = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    print(s.search(nums, target))