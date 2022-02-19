from tree.TreeBuilder import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        
        def preorder(node):
            nonlocal ans
            
            if not node:
                ans.append("#")
                return
            
            ans.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return ",".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        i = 0
        data = data.split(",")
        
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
        
        return preorder()


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
    
    
    n0 = TreeNode(3)

    n1 = TreeNode(12)
    n2 = TreeNode(20)
    n3 = TreeNode(15, n1, n2)
    
    n4 = TreeNode(10, n0, n3)

    n4.display()
    ans = deser.deserialize(ser.serialize(n4))
    ans.display()