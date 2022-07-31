from typing import List
from TreeBuilder import TreeNode



def get_height(root):
    if root is None:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        height = get_height(root) - 1
        m = height+1
        n = 2**(height+1) - 1
        res = [[""] * n for _ in range(m)]

        def preorder(root, r, c):
            nonlocal res
            if root is None:
                return
            res[r][c] = str(root.val)
            preorder(root.left, r+1, c-2**(height-r-1))
            preorder(root.right, r+1, c+2**(height-r-1))
        
        preorder(root, 0, n//2)
        return res


