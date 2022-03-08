from typing import List, Optional
from TreeBuilder import TreeNode


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        childs = set()
        nodes = dict()
        for p_val, c_val, is_left in descriptions:
            if p_val not in nodes:
                nodes[p_val] = TreeNode(p_val)
            if c_val not in nodes:
                nodes[c_val] = TreeNode(c_val)
            if is_left:
                nodes[p_val].left = nodes[c_val]
            else:
                nodes[p_val].right = nodes[c_val]
            
            childs.add(c_val)
        
        head_val = (nodes.keys() - childs).pop()
        return nodes[head_val]

if __name__ == '__main__':
    s = Solution()
    ans = s.createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])
    ans.display()

    ans = s.createBinaryTree([[1,2,1],[2,3,0],[3,4,1]])
    ans.display()

    ans = s.createBinaryTree([[39,70,1],[13,39,1],[85,74,1],[74,13,1],[38,82,1],[82,85,1]])
    ans.display()