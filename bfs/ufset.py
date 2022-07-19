class UnionFindSet:

    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.connected = size
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            self.parents[root2] = root1
            self.connected -= 1

    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]
    
    def is_connected(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        return root1 == root2
    
    def count_connected(self):
        return self.connected
    
        