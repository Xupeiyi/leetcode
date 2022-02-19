from TreeBuilder import TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums) -> TreeNode:
        if not nums:
            return None
            
        maximum = -1
        max_idx = -1
        for i, num in enumerate(nums):
            if num > maximum:
                maximum = num
                max_idx = i
        
        left = self.constructMaximumBinaryTree(nums[:max_idx])
        right = self.constructMaximumBinaryTree(nums[max_idx+1:])
        return TreeNode(maximum, left, right)


if __name__ == '__main__':
    s = Solution()
    ans = s.constructMaximumBinaryTree([3, 2, 1])
    ans.display()