from trace import Trace
from typing import List
from TreeBuilder import TreeNode



class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        if len(preorder) == 0 and len(postorder) == 0:
            return None
        
        elif len(preorder) == 1 and len(postorder) == 1:
            return TreeNode(preorder[0])
        
        root = TreeNode(postorder[-1])
        right_root_idx = preorder.index(postorder[-2])
        right_tree_size = len(preorder) - right_root_idx
        right_preorder, right_postorder = preorder[right_root_idx:], postorder[-1-right_tree_size:-1]
        left_preorder, left_postorder = preorder[1:right_root_idx], postorder[:-1-right_tree_size]

        root.left = self.constructFromPrePost(left_preorder, left_postorder)
        root.right = self.constructFromPrePost(right_preorder, right_postorder)

        return root

if __name__ == '__main__':
    s = Solution()
    ans = s.constructFromPrePost([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1])
    ans.display()