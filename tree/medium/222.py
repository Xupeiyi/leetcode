from TreeBuilder import TreeNode

# -----------------------------------
# Solution1


def findWidth(root):
    width = -1
    while root:
        width += 1
        root = root.left
    return width


def dec_to_bin(num, width):
    bin_exp = bin(num)[2:]
    bin_exp = '0' * (width - len(bin_exp)) + bin_exp
    return bin_exp
    
    
def checkNode(root, width, idx):
    path = dec_to_bin(idx, width)
    ans = root
    for p in path:
        if p == '0':
            ans = ans.left
        elif p == '1':
            ans = ans.right
    return ans is not None


def countLastLevel(root, width):
    start = 0
    end = 2 ** width - 1
    if checkNode(root, width, end):
        return end
    
    while start <= end:
        mid = (start + end) // 2
        
        if checkNode(root, width, mid):
            start = mid + 1
        else:
            end = mid - 1
    return end



class Solution1:
    def countNodes(self, root):
        # 求树深度
        if not root:
            return 0
        width = findWidth(root)
        if not width:
            return 1
        last_level_num = countLastLevel(root, width)
        return 2**width + last_level_num

        
# --------------------------------------------------
# Solution2

def is_complete(root):
    if not root:
        return 0
    left = root.left
    l_height = 1
    right = root.right
    r_height = 1
    
    while left:
        l_height += 1
        left = left.left
    
    while right:
        r_height += 1
        right = right.right
    
    if l_height == r_height:
        return l_height
    else:
        return 0


class Solution:
    def countNodes(self, root):
        """尽管本身不是完全二叉树， 但可以由多个完全二叉树组成"""
        if not root:
            return 0
        
        num = 1
        l_height = is_complete(root.left)
        r_height = is_complete(root.right)
        
        num += 2**l_height - 1 if l_height else self.countNodes(root.left)
        num += 2**r_height - 1 if r_height else self.countNodes(root.right)
        
        return num
        
        
        
if __name__ == '__main__':
    # w = 4
    # i = 3
    # a = countLastLevel([i for i in range(i)] + [None] * (2**w-i), w)
    # print(a)
    # print(dec_to_bin(5, 3))
    
    n0 = TreeNode(4)
    n1 = TreeNode(5)
    n2 = TreeNode(2, n0, n1)
    
    n3 = TreeNode(6)
    n4 = TreeNode(3, n3)
    
    n5 = TreeNode(1, n2, n4)
    n5.display()
    
    s = Solution1()
    # w = findWidth(n5)
    # print(w)
    # print(countLastLevel(n5, w))
    print(s.countNodes(n5))
    
    
    