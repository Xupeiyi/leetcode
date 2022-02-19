# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: TreeNode) -> int:
    if root == None:
        return 0
    else:
        return 1 + max(maxDepth(root.left), maxDepth(root.right))


t0 = TreeNode(15)
t1 = TreeNode(7)
t2 = TreeNode(20, t0, t1)
t3 = TreeNode(9)
t4 = TreeNode(3, t2)
print(maxDepth(t4))

"""
performace
time   56  31  10  16  55
space  36  74  56  61  75
"""
        