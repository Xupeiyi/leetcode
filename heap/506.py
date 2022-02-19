from queue import PriorityQueue


class Solution:
    def findRelativeRanks(self, score):
        ranking = ("Gold Medal", "Silver Medal", "Bronze Medal")
        q = PriorityQueue()
        for pos, sc in enumerate(score):
            q.put([-sc, pos])
        
        ans = [""] * len(score)
        rank = 0
        while not q.empty():
            _, pos = q.get()
            ans[pos] = ranking[rank] if rank < 3 else str(rank + 1)
            rank += 1
        return ans
    
    
if __name__ == '__main__':
    s = Solution()
    
    print(s.findRelativeRanks([10, 3, 8, 9, 4]))
    
    