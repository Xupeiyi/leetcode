# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution1:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        path = [node]
        new_node = Node(node.val)
        cloned = {node: new_node}  # record whether a node has been cloned or not
        while path:
            curr = path.pop(0)
            
            for neighbor in curr.neighbors:
                # next node to traverse
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val)
                    path.append(neighbor)
                
                # clone neighbors
                cloned[curr].neighbors.append(cloned[neighbor])
                
        return new_node
        

        
        
def traverse(node):
    visited = set()
    path = [node]
    
    while path:
        curr = path.pop(0)
        if curr not in visited:
            visited.add(curr)
            print(curr.val)
            for neighbor in curr.neighbors:
                path.append(neighbor)
        
# 2nd trial on 07/15/2023
class Solution2:

    cloned = {}

    def cloneGraph(self, node: 'Node'):
        if node is None:
            return None

        if node in self.cloned:
            return self.cloned[node]
        
        self.cloned[node] = Node(val=node.val)

        for neighbor in node.neighbors:
            n = self.cloneGraph(neighbor)
            self.cloned[node].neighbors.append(n)

        return self.cloned[node]
        

if __name__ == '__main__':
    s = Solution2()

    n1 = Node(2)
    n4 = Node(4)

    n3 = Node(3, [n1, n4])
    n0 = Node(1, [n1, n4])
    
    n1.neighbors = [n0, n3]
    n4.neighbors = [n0, n3]
    
    new_n0 = s.cloneGraph(n0)
    traverse(new_n0)