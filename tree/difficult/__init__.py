from tree.TreeBuilder import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = ""
        
        def preorder(node):
            nonlocal ans
            
            if not node:
                ans += "#"
                return
            
            ans += str(node.val)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        i = 0
        
        def preorder():
            nonlocal i
            if i >= len(data):
                return
            
            if data[i] == '#':
                i += 1
                return None
            
            val = int(data[i])
            i += 1
            left = preorder()
            right = preorder()
            return TreeNode(val, left, right)
        
        ans = preorder()
        return ans


if __name__ == '__main__':
    ser = Codec()
    deser = Codec()
    
    n0 = TreeNode(1)
    n1 = TreeNode(2, n0)
    n2 = TreeNode(4)
    n3 = TreeNode(3, n1, n2)
    n3.display()
    sered = ser.serialize(n3)
    print(sered)
    
    ans = deser.deserialize(sered)
    ans.display()