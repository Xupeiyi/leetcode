from typing import List
from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        nnodes = len(graph)
        visited = [False for _ in range(nnodes)]
        color = [False for _ in range(nnodes)]
        
        def bfs(root):
            nonlocal visited
            nonlocal color
            neigbors = deque([root])
            visited[root] = True
            while neigbors:
                node = neigbors.popleft()

                for adjacent in graph[node]:
                    if visited[adjacent] and color[adjacent] == color[node]:
                        return False
                    if not visited[adjacent]:
                        color[adjacent] = not color[node]
                        visited[adjacent] = True
                        neigbors.append(adjacent)
            
            return True
        
        for node in range(nnodes):
            if not visited[node] and not bfs(node):
                return False
            
        return True


if __name__ == '__main__':
    graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
    s = Solution()
    ans = s.isBipartite(graph)
    print(ans)