from TreeBuilder import TreeNode


def buildTrees(idx, value_range):
    if not value_range:
        return [None]
    
    length = len(value_range)
    
    lefts = []
    for i in range(idx):
        lefts += buildTrees(i, value_range[:idx])
    lefts = lefts if lefts else [None]
    
    rights = []
    for i in range(length-idx-1):
        rights += buildTrees(i, value_range[idx+1:])
    rights = rights if rights else [None]
    
    return [TreeNode(value_range[idx], l, r) for l in lefts for r in rights]


class Solution:
    def generateTrees(self, n: int):
        ans = []
        values = [i+1 for i in range(n)]
        for i in range(n):
            ans += buildTrees(i, values)
        return ans
    
    
if __name__ == '__main__':
    s = Solution()
    ans = s.generateTrees(3)
    for t in ans:
        t.display()

