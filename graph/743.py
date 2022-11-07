import math
from typing import List
from queue import PriorityQueue
from collections import defaultdict


def build_graph(times, n):
    graph = defaultdict(list)
    for from_, to, weight in times:
        graph[from_-1].append((to-1,  weight))
    return graph



class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = build_graph(times, n)
        dists = [math.inf] * n
        dists[k-1] = 0

        queue = PriorityQueue()
        queue.put((0, k-1))

        while not queue.empty():
            total_dist, node = queue.get()
            if dists[node] < total_dist:
                continue
            for adjacent, weight in graph[node]:
                dist_adj = weight + dists[node]
                if dist_adj < dists[adjacent]:
                    dists[adjacent] = dist_adj
                    queue.put((dist_adj, adjacent))
        
        ans = max(dists)
        return ans if ans != math.inf else -1





if __name__ == '__main__':
    times = [[2,1,1],[2,3,1],[3,4,1]]
    g = build_graph(times, 4)
    print(g)
    s = Solution()
    ans = s.networkDelayTime(times, 4, 2)
    print(ans)