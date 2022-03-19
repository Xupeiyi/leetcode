from typing import List
from collections import defaultdict, deque

# 在这里出过bug
# 错误写法：
# def find_dists(graph):
#     dists = {0: 0}
#     paths = [graph[0]]
#     curr_length = 0
#     while paths:
#         path = paths.pop(0)
#         curr_length += 1
#         for node in path:
#             if node not in dists:
#                 dists[node] = curr_length
#                 next_path = graph[node] - dists.keys()
#                 if next_path:
#                     paths.append(next_path)
#     return dists


def find_dists(graph):
    dists = [-1]*len(graph)
    dists[0] = 0
    nodes = deque([0])

    while nodes:
        node = nodes.popleft()
        for adjacent in graph[node]:
            if dists[adjacent] == -1:
                dists[adjacent] = dists[node] + 1 
                nodes.append(adjacent)
    return dists


def latest_receive_time(dist, patience):
    if not patience:
        return 0
    nresends =  (2 * dist - 1) // patience
    return nresends*patience + 2*dist    


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        graph = defaultdict(list)
        for from_, to in edges:
            graph[from_].append(to)
            graph[to].append(from_)
        dists = find_dists(graph)
        return max([latest_receive_time(dists[i], p) for i, p in enumerate(patience)]) + 1
        

if __name__ == '__main__':
    s = Solution()
    ans = s.networkBecomesIdle([[0, 1], [1, 2]], [0, 2, 1])
    print(ans)
    