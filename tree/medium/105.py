from TreeBuilder import TreeNode


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder and not inorder:
            return None
        # find head node in inorder list
        head = preorder.pop(0)
        head_idx = inorder.index(head)
        
        # build left tree
        preorder_left = preorder[0:head_idx]
        inorder_left = inorder[0:head_idx]
        left = self.buildTree(preorder_left, inorder_left)

        # build right tree
        preorder_right = preorder[head_idx:]
        inorder_right = inorder[head_idx+1:]
        right = self.buildTree(preorder_right, inorder_right)

        return TreeNode(head, left, right)


if __name__ == '__main__':
    s = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    head = s.buildTree(preorder, inorder)
    head.display()