from TreeBuilder import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)
        
        ancester = root
        while not (min_val <= ancester.val <= max_val):
            if ancester.val < min_val:
                ancester = ancester.right
            elif ancester.val > max_val:
                ancester = ancester.left
        
        return ancester

if __name__ == '__main__':
    s = Solution()
    
    n0 = TreeNode(3)
    n1 = TreeNode(5)
    n2 = TreeNode(4, n0, n1)
    
    n3 = TreeNode(0)
    n4 = TreeNode(2, n3, n2)
    
    n5 = TreeNode(7)
    n6 = TreeNode(9)
    n7 = TreeNode(8, n5, n6)
    n8 = TreeNode(6, n4, n7)
    n8.display()
    ans = s.lowestCommonAncestor(n8, n0, n1)
    print(ans.val)