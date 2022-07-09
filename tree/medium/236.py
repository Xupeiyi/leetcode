from re import L
from TreeBuilder import TreeNode

##################################
# Solution 1
##################################


class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        paths = [[root]]
        p_path, q_path = [], []
        
        while paths:
            path = paths.pop()
            end = path[-1]
            if end.val == p.val:
                p_path = path
                continue
            if end.val == q.val:
                q_path = path
                continue
            if not (p_path and q_path):
                if end.right:
                    paths.append(path + [end.right])
                if end.left:
                    paths.append(path + [end.left])
            else:
                break
        ancestor = root
        if p_path and q_path:
            for p_node, q_node in zip(p_path, q_path):
                if p_node == q_node:
                    ancestor = p_node
                else:
                    break
        else:
            ancestor = (p_path + q_path)[-1]
        
        return ancestor

##################################
# Solution 2
##################################

class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        elif not left and right:
            return right
        elif not right and left:
            return left
        else:
            return None

# 2022.6.5
# -----------------------------------------------
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root.val == p.val or root.val == q.val:
            return root
        
        ancestor_left = self.lowestCommonAncestor(root.left, p, q)
        ancestor_right = self.lowestCommonAncestor(root.right, p, q)

        if ancestor_left and ancestor_right:
            return root
        elif ancestor_left and not ancestor_right:
            return ancestor_left
        elif not ancestor_left and ancestor_right:
            return ancestor_right
        else:
             return None



if __name__ == '__main__':
    s = Solution1()
    
    n0 = TreeNode(7)
    n1 = TreeNode(4)
    n2 = TreeNode(2, n0, n1)
    n3 = TreeNode(5, None, n2)
    n4 = TreeNode(3, n3)
    
    ans = s.lowestCommonAncestor(n4, n3, n1)
    print(ans.val)