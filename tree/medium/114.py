from TreeBuilder import TreeNode

# -----------------------------------------
# Solution1

class Solution1:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        if not root.left and not root.right:
            return root 
        start, _ = self.tree_to_list(root)
        root.left = start.left
        root.right = start.right


    def tree_to_list(self, root):
        # 占用空间过多，需优化
        start = end = TreeNode(root.val, None, None)

        if not root.left and not root.right:
            return start, end # 不能返回root, root, 会产生bug, 因为root是一个引用。应该返回深拷贝。

        if root.right and not root.left:
            rhead, rend = self.tree_to_list(root.right)
            start.right = rhead
            end = rend

        if root.left and not root.right:
            lhead, lend = self.tree_to_list(root.left)
            start.right = lhead
            end = lend
        
        if root.left and root.right:
            rhead, rend = self.tree_to_list(root.right)
            lhead, lend = self.tree_to_list(root.left)
            lend.right = rhead
            start.right = lhead
            end = rend
        
        return start, end


# ---------------------------------------------------
# Solution2

class Solution2:
    def flatten(self, root):
        if not root:
            return
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        if root.left:
            lend = root.left
            while lend.right:
                lend = lend.right
            
            lend.right = root.right
            root.right = root.left
            root.left = None
        
        return


# ---------------------------------------------------
# Solution3

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.tree_to_list(root)

    def tree_to_list(self, root):
        """返回链表最后一个节点"""
        if not root:
            return None
        
        if not root.left and not root.right:
            return root
        
        rend = self.tree_to_list(root.right)
        lend = self.tree_to_list(root.left)
        
        if lend:
            lend.right = root.right
            root.right = root.left
            root.left = None
        
        return rend if rend else lend


if __name__ == '__main__':
    s = Solution()

    n0 = TreeNode(3)
    n1 = TreeNode(4, n0)
    n2 = TreeNode(2, n1)
    n2.display()
    s.flatten(n2)
    n2.display()
    

        


