from TreeBuilder import TreeNode

class Solution:

    def tree2str(self, root):
        if root is None:
            return ""

        lstr = self.tree2str(root.left)
        rstr = self.tree2str(root.right)
        
        if not lstr and not rstr:
            childstr = ""
        elif not rstr:
            childstr = f"({lstr})"
        else:
            childstr = f"({lstr})({rstr})"
        return f"{root.val}{childstr}"