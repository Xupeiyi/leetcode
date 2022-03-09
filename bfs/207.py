from typing import List
from collections import defaultdict, deque

# 拓扑排序
# 如何判断图中是否有环？
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list)
        indeg = [0] * numCourses  # 记录入度

        # 邻接表
        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1

        q = deque([u for u in range(numCourses) if indeg[u] == 0])
        visited = 0

        # 通过bfs不断删除入度为0的结点。如果有环，则一定无法删除全部结点
        while q:
            visited += 1
            u = q.popleft()
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        
        return visited == numCourses