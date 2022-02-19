from TreeBuilder import TreeNode

########################################
# 初次尝试
########################################
def sumPath(path):
    return sum(p * 10 ** i for i, p in enumerate(reversed(path)))

class Solution1:
    def sumNumbers(self, root):
        paths = [[root]]
        complete_paths = []
        while paths:
            path = paths.pop()
            end = path[-1]
            if end.right:
                paths.append(path + [end.right])
            if end.left:
                paths.append(path + [end.left])
            if not end.right and not end.left:
                complete_paths.append([node.val for node in path])
        
        return sum(sumPath(path) for path in complete_paths)


############################################
# 改进后
############################################

class Solution:
    def sumNumbers(self, root):
        nodes = [root]
        path_sums = [root.val]
        total_sum = 0
        while nodes:
            node = nodes.pop()
            path_sum = path_sums.pop()
            if node.right:
                nodes.append(node.right)
                path_sums.append(path_sum*10+node.right.val)
            if node.left:
                nodes.append(node.left)
                path_sums.append(path_sum*10+node.left.val)
            if not node.right and not node.left:
                total_sum += path_sum
            
        return total_sum
        
        
if __name__ == '__main__':
    s = Solution()
    n0 = TreeNode(2)
    n1 = TreeNode(3)
    n2 = TreeNode(1, n0, n1)
    a = s.sumNumbers(n2)
    print(a)