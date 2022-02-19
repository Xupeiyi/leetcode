class NestedInteger:
    
    def __init__(self, initializer):
        self.val = None
        self.list = None
        if isinstance(initializer, int):
            self.val = initializer
        elif isinstance(initializer, list):
            self.list = initializer
    
    def isInteger(self):
        return self.val is not None
    
    def getInteger(self):
        return self.val
    
    def getList(self):
        return self.list
    

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.ends = [ni for ni in nestedList]
        self.searchForInteger()
    
    def next(self) -> int:
        ans = self.ends.pop(0).getInteger()
        self.searchForInteger()
        return ans
            
    def hasNext(self) -> bool:
        return bool(self.ends)
    
    def searchForInteger(self):
        # dfs the tree until the next integer is ready for output
        while self.hasNext():
            if not self.ends[0].isInteger():
                end = self.ends.pop(0)
                for successor in reversed(end.getList()):
                    self.ends.insert(0, successor)
            else:
                break
        
        
        
if __name__ == '__main__':

    n0 = NestedInteger(1)
    n1 = NestedInteger(3)
    n2 = NestedInteger([n0, n1])
    
    n3 = NestedInteger(2)
    
    n4 = NestedInteger(1)
    n5 = NestedInteger(1)
    n6 = NestedInteger([n4, n5])
    
    i, v = NestedIterator([n2, n3, n6]), []
    
    print(i.hasNext())
    
    while i.hasNext():
        v.append(i.next())
    
    print(v)