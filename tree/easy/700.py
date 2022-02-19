class Solution:
    def searchBST(self, root, val: int):
        if not root or root.val == val:
            return root
        
        if root.val > val:
            self.searchBST(root.left, val)
        else:
            self.searchBST(root.right, val)