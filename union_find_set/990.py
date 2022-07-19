from typing import List
from ufset import UnionFindSet

def idx(x):
    return ord(x) - ord('a')

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFindSet(26)

        for equation in equations:
            var1, eq, var2 = equation[0], equation[1:3], equation[3]
            if eq == '==':
                uf.union(idx(var1), idx(var2))
        
        for equation in equations:
            var1, eq, var2 = equation[0], equation[1:3], equation[3]
            if eq == '!=' and uf.is_connected(idx(var1), idx(var2)):
                return False
        
        return True
                

