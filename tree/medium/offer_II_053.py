from TreeBuilder import TreeNode

class Solution:

    def first_left_node(self, root):
        while root.left:
            root = root.left
        return root

    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        previous = None # the node that is searched before node
        while root:
            if p.val == root.val:
                # if p has right child, return the first left node of right child
                return self.first_left_node(p.right) if p.right else previous
            elif p.val < root.val:
                # if the target is in the left child of root, 
                # then target's successor could be root
                previous = root
                root = root.left
            else:
                root = root.right

        return None


if __name__ == '__main__':
    s = Solution()
    
    # test1
    n0 = TreeNode(2) 
    n1 = TreeNode(4)
    n2 = TreeNode(3, n0, n1)
    n3 = TreeNode(6, n2)
    n3.display()

    ans = s.inorderSuccessor(n3, n1)   
    print(ans.val == 6)

    # test2

    n0 = TreeNode(2) 
    n4 = TreeNode(3.5)
    n1 = TreeNode(4, n4)
    n2 = TreeNode(3, n0, n1)
    n2.display()

    ans = s.inorderSuccessor(n2, n1)   
    print(ans)


    # test3
    n0 = TreeNode(2)
    n4 = TreeNode(5)
    n1 = TreeNode(4, None, n4)
    n2 = TreeNode(3, n0, n1)
    n3 = TreeNode(6, n2)
    n3.display()

    ans = s.inorderSuccessor(n3, n1)   
    print(ans.val == 5)


    # test4
    n0 = TreeNode(1)
    n1 = TreeNode(3)
    n2 = TreeNode(2, n0, n1)
    n2.display()
    ans = s.inorderSuccessor(n2, n0)
    print(ans.val)

