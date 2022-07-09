from typing import List
from collections import defaultdict, Counter

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        size = len(parents)
        children = defaultdict(list)
        for i, parent in enumerate(parents):
            children[parent].append(i)
        children.pop(-1)

        tree_size = [1 for _ in range(size)]
        def dfs(root):
            nonlocal tree_size
            nonlocal children
            if root not in children:
                return
            for child in children[root]:
                dfs(child)
            tree_size[root] = sum(tree_size[child] for child in children[root]) + 1
        dfs(0)

        ans = Counter()
        for node in range(size):
            if node not in children:
                ans[size - 1] += 1
            else:
                product = tree_size[0] - tree_size[node] if node != 0 else 1
                for child in children[node]:
                    product *= tree_size[child]
                ans[product] += 1

        return ans[max(ans.keys())]




if __name__ == '__main__':
    s = Solution()
    ans = s.countHighestScoreNodes([-1,3,3,5,7,6,0,0])
    print(ans)