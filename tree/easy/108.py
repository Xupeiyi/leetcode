from TreeBuilder import TreeNode

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums)//2
        left = self.sortedArrayToBST(nums[:mid])
        right = self.sortedArrayToBST(nums[mid+1:])
        return TreeNode(nums[mid], left, right)


if __name__ == '__main__':
    s = Solution()
    ans = s.sortedArrayToBST([-10, -3, 0, 5, 9])
    ans.display()