from TreeBuilder import TreeNode


class Solution:
    def pathSum(self, root, targetSum):
        ans = []
        
        def backtrack(node, sum_, path):
            nonlocal ans
            if not node:
                return
            
            curr_sum = sum_ + node.val
            curr_path = path + [node.val]
            
            if curr_sum == targetSum and not node.left and not node.right:
                ans.append(curr_path)
            if node.left:
                backtrack(node.left, curr_sum, curr_path)
            if node.right:
                backtrack(node.right, curr_sum, curr_path)
        
        backtrack(root, 0, [])
        return ans
    
    
if __name__ == '__main__':
    s = Solution()
    
    n0 = TreeNode(4)
    n1 = TreeNode(8)
    n2 = TreeNode(5, n0, n1)
    
    ans = s.pathSum(n2, 9)
    print(ans)