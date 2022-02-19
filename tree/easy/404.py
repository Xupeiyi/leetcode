from TreeBuilder import TreeNode


def left_sum(root, is_left):
    if not root:
        return 0

    if not root.left and not root.right and is_left:
        return root.val
    
    sum = 0
    sum += left_sum(root.left, True)
    sum += left_sum(root.right, False)
    return sum

    
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return left_sum(root, False)
    
    
