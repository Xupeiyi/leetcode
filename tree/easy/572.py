class TreeNode:
    def __init__(self, name, val=0, left=None, right=None):
        self.name = name
        self.val = val
        self.left = left
        self.right = right


def is_equal_tree(t1, t2):
    if not t1 and not t2:
        return True

    if not t1 or not t2:
        return False
    
    return t1.val == t2.val \
           and is_equal_tree(t1.left, t2.left) \
           and is_equal_tree(t1.right, t2.right)
    

class Solution:

    def isSubtree(self, root: TreeNode, subRoot: TreeNode):
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False

        return is_equal_tree(root, subRoot) \
               or self.isSubtree(root.left, subRoot) \
               or self.isSubtree(root.right, subRoot)


if __name__ == '__main__':
    s = Solution()
    # 1
    # n0 = TreeNode(1)
    # n1 = TreeNode(4, n0)

    # n2 = TreeNode(1)
    # n3 = TreeNode(4, n2)
    # n4 = TreeNode(5, n3)
    
    # print(is_equal_tree(n1, n3))
    # print(s.isSubtree(n4, n1))


    # 2
    n0 = TreeNode('n0', 2)
    n1 = TreeNode('n1', 1, n0)
    n2 = TreeNode('n2', 1, None, n1)
    n3 = TreeNode('n3', 1, None, n2)
    n4 = TreeNode('n4', 1, None, n3)


    n5 = TreeNode('n5', 1, None, n4)
    n6 = TreeNode('n6', 1, None, n5)

    print(s.isSubtree(n6, n4))

    
        

