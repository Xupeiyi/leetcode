from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        

class Solution:

    def pre_traverse(self, root, ans):
        if not root:
            return
        ans.append(root.val)
        for child in root.children:
            self.pre_traverse(child, ans)

    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        self.pre_traverse(root, ans)
        return ans
