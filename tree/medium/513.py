from TreeBuilder import TreeNode





class Solution:
    def findBottomLeftValue(self, root) -> int:
        ans = root.val
        max_depth = 0
        
        def preorder(node, is_left, depth):
            nonlocal ans, max_depth
            if not node:
                return 
            if not node.left and not node.right and is_left:
                if depth > max_depth:
                    max_depth = depth
                    ans = node.val
            
            preorder(node.left, True, depth+1)
            preorder(node.right, False, depth+1)
        
        preorder(root, True, 0)
        return ans