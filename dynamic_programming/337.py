from tree.medium.TreeBuilder import TreeNode


def get_val(node):
    return node.val if node else 0


def dp(root):

    if not root:
        return None
    
    left = dp(root.left) if root.left else None
    right = dp(root.right) if root.right else None
    
    rob_root = root.val
    if root.left:
        rob_root += (get_val(left.left) + get_val(left.right))
    if root.right:
        rob_root += (get_val(right.left) + get_val(right.right))
    
    val = max(rob_root, get_val(left) + get_val(right))
    
    return TreeNode(val, left, right)


class Solution:
    
    def rob(self, root: TreeNode) -> int:
        dp_root = dp(root)
        dp_root.display()
        return max(dp_root.val, get_val(dp_root.left) + get_val(dp_root.right))
        


if __name__ == '__main__':
    s = Solution()
    
    n0 = TreeNode(3)
    n1 = TreeNode(2, n0)
    
    n2 = TreeNode(1)
    n3 = TreeNode(3, n2)
    
    n4 = TreeNode(3, n1, n3)
    n4.display()
    
    ans = s.rob(n4)
    print(ans)
    
    
    n0 = TreeNode(1)
    n1 = TreeNode(3)
    n2 = TreeNode(4, n0, n1)
    
    n3 = TreeNode(1)
    n4 = TreeNode(5, n3)
    
    n6 = TreeNode(3, n2, n4)
    n6.display()
    ans = s.rob(n6)
    print(ans)
    
    
    n0 = TreeNode(4)
    n1 = TreeNode(1, n0)
    n2 = TreeNode(3)
    n3 = TreeNode(2, n1, n2)
    n3.display()
    ans = s.rob(n3)
    print(ans)
    
    n0 = TreeNode(3)
    n1 = TreeNode(2, n0)
    n2 = TreeNode(1, n1)
    n3 = TreeNode(4, n2)
    n3.display()
    ans = s.rob(n3)
    print(ans)
    