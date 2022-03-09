from typing import List
from collections import defaultdict, deque

class Solution:
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