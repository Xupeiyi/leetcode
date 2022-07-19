from typing import List
from collections import defaultdict, deque

class Solution1:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0] * numCourses
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indeg[course] += 1
        
        q = deque([course for course in range(numCourses) if indeg[course] == 0])
        order = []
        
        while q:
            prereq = q.popleft()
            order.append(prereq)
            for course in graph[prereq]:
                indeg[course] -= 1
                if not indeg[course]:
                    q.append(course)
        return order if len(order) == numCourses else []




def build_graph(prerequisites):
    graph = defaultdict(list)
    for prerequsite in prerequisites:
        graph[prerequsite[1]].append(prerequsite[0])
    return graph


# 使用DFS（回溯）判断是否成环
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = build_graph(prerequisites)
        visited = [False for _ in range(numCourses)]
        on_path = [False for _ in range(numCourses)]
        has_cycle = False
        
        postorder = []

        def dfs(node):
            nonlocal has_cycle
            nonlocal graph
            nonlocal visited
            nonlocal on_path
            nonlocal postorder
            
            if on_path[node]:
                has_cycle = True
                return
            
            if visited[node] or has_cycle:
                return

            visited[node] = True
            
            on_path[node] = True
            for adjacent in graph[node]:
                dfs(adjacent)
            on_path[node] = False
            postorder.append(node)

        
        for node in range(numCourses):
            dfs(node)
        
        return [] if has_cycle else postorder[::-1]
