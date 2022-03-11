from typing import List

# 表示树的方法并不只有建立结点喔
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        children = [[] for _ in range(n)] 
        for child, parent in enumerate(parents):
            if parent != -1:
                children[parent].append(child)
        
        max_score, count = 0, 0
        def dfs(node: int) -> int:
            nonlocal max_score, count
            score = 1
            rest_size = n - 1
            
            for child in children[node]:
                child_size = dfs(child)
                score *= child_size
                rest_size -= child_size
            
            if node != 0:
                score *= rest_size
            
            if score == max_score:
                count += 1
            elif score > max_score:
                max_score = score
                count = 1
            
            return n - rest_size
        
        dfs(0)
        return count