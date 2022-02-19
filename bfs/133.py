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
        

if __name__ == '__main__':
    s = Solution()

    n1 = Node(2)
    n4 = Node(4)

    n3 = Node(3, [n1, n4])
    n0 = Node(1, [n1, n4])
    
    n1.neighbors = [n0, n3]
    n4.neighbors = [n0, n3]
    
    new_n0 = s.cloneGraph(n0)
    
    traverse(new_n0)