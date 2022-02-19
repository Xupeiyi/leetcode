from TreeBuilder import TreeNode


class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        if not inorder and not postorder:
            return None

        # find head node in inorder list
        root = postorder.pop(-1)
        root_idx = inorder.index(root)
        
        # build left tree
        inorder_left = inorder[0:root_idx]
        postorder_left = postorder[0:root_idx]

        left = self.buildTree(inorder_left, postorder_left)

        # build right tree
        inorder_right = inorder[root_idx+1:]
        postorder_right = postorder[root_idx:]
        right = self.buildTree(inorder_right, postorder_right)

        return TreeNode(root, left, right)


if __name__ == '__main__':
    s = Solution()
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]

    head = s.buildTree(inorder, postorder)
    head.display()