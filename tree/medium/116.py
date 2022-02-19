from TreeBuilder import TreeNode

TreeNode.next = None
# -------------------------------------------------
# solution1: 层序遍历


class Solution1:
    def connect(self, root):
        if not root:
            return
        ends = [root]
        
        while ends:
            new_ends = []
            for i, end in enumerate(ends):
                ends[i].next = ends[i+1] if i < len(ends) - 1 else None
                
                if end.left and end.right:
                    new_ends.append(end.left)
                    new_ends.append(end.right)
            ends = new_ends
            
        return root


# ------------------------------------------
# Solution 2: 后序遍历

def connect_nodes(root1, root2):
    if not root2 and not root2:
        return
    
    connect_nodes(root1.left, root1.right)
    connect_nodes(root2.left, root2.right)
    connect_nodes(root1.right, root2.left)
    
    root1.next = root2


class Solution:
    def connect(self, root):
        connect_nodes(root.left, root.right)
        

def next_val(node):
    return node.next.val if node.next else None
    
    
if __name__ == '__main__':
    s = Solution()
    n0 = TreeNode(1)
    n1 = TreeNode(2)
    n2 = TreeNode(3, n0, n1)
    
    n3 = TreeNode(4)
    n4 = TreeNode(5)
    n5 = TreeNode(6, n3, n4)
    
    n6 = TreeNode(7, n2, n5)
    
    s.connect(n6)
    n6.display()
    
    for node in [n0, n1, n2, n3, n4, n5, n6]:
        print(str(node.val) + "->" + str(next_val(node)))
    # next_val(n1)
    # next_val(n3)
    # next_val(n4)
    # next_val(n2)
    # next_val(n5)
    # next_val(n6)
    
