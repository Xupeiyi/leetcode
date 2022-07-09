from TreeBuilder import TreeNode
import collections
from typing import Optional, List


class Solution:

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        """序列化整颗树的子树序列, 如果已存在这样的子树, 则输出
        """
        res = []
        counter = collections.Counter()
        
        def traverse(root):
            if not root: return '#'
            left = traverse(root.left)
            right = traverse(root.right)
            chain = left + ',' + right + ',' + str(root.val)
            counter[chain] += 1
            if counter[chain] == 2: res.append(root)
            return chain
        
        traverse(root)
        return res


# 2022-06-05
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        traversed = set()
        ans = []
        def serialize(root):
            nonlocal traversed
            if not root:
                return '#'

            sl = serialize(root.left)
            sr = serialize(root.right) 
            serial = sl + sr + str(root.val)

            if serial in traversed:
                ans.append(root)
            
            traversed.add(serial)
            return serial
        serialize(root)
        return ans
        
        