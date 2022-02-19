from TreeBuilder import TreeNode

# 初次尝试。
# 想到了总是保留左子树，但没想到如何保存左子树的父节点，所以选择了总是保存根节点的做法
# 答案：使用栈，并迭代。
class BSTIterator0:

    def __init__(self, root):
        self.root = root
        self.left_half = self.left_half_traversal(root) # 遍历左子树并保存，占用的空间依然为O(n)
    
    def left_half_traversal(self, root):
        if not root:
            return []
        return self.inorder_traversal(root.left) + [root]
    
    def inorder_traversal(self, root):
        if not root:
            return []
        return self.inorder_traversal(root.left) + [root] + self.inorder_traversal(root.right)

    def next(self):
        if not self.root:
            return None

        if not self.left_half:
            self.left_half = self.left_half_traversal(self.root.right)
            self.root = self.root.right

        return self.left_half.pop(0).val if self.left_half else None

    def hasNext(self):
        if not self.root:
            return False

        return bool(self.left_half or self.root.right) 


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self._stack = []
        self._add(root)

    def _add(self, node):
        """节点入栈后，入栈左节点"""
        while node:
            self._stack.append(node)
            node = node.left

    def _pop(self):
        """节点出栈后，入栈右节点"""
        node = self._stack.pop(-1)
        self._add(node.right)
        return node.val


    def next(self) -> int:
        """节点入栈后，入栈左节点。出栈后，将右结点"""
        return self._pop()

    def hasNext(self) -> bool:
        return len(self._stack) > 0 



# 解法 2
class BSTIterator1(object):

    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        cur = self.stack.pop()
        node = cur.right
        while node:
            self.stack.append(node)
            node = node.left
        return cur.val

    def hasNext(self):
        return len(self.stack) > 0




if __name__ == '__main__':
    n = TreeNode(-1)
    n0 = TreeNode(3, n)
    n1 = TreeNode(9)
    n2 = TreeNode(20)
    n3 = TreeNode(15, n1 ,n2)
    n4 = TreeNode(7, n0, n3)
    n4.display()
    b = BSTIterator(n4)

    print(b.next())
    print(b.next())
    print(b.hasNext())
    
    print(b.next())
    print(b.hasNext())
    
    print(b.next())
    print(b.hasNext())
    print(b.next())
    print(b.hasNext())
    #print(b.next())
    # print(b.hasNext())
    #print(b.next())


    print('============================')
    n0 = TreeNode(2)
    n1 = TreeNode(1, None, n0)
    n2 = TreeNode(4)
    n3 = TreeNode(3, n1, n2)
    n3.display()
    b = BSTIterator(n3)
    while b.hasNext():
        print(b.next())



