from typing import List
from itertools import accumulate
from random import randrange

class Solution:

    def __init__(self, w: List[int]):
        self.cumsum_w = [0] + list(accumulate(w))

    def pickIndex(self) -> int:
        start = 1
        end = len(self.cumsum_w) - 1

        while start < end:
            mid = (start + end) // 2
            picked = randrange(self.cumsum_w[start-1] + 1, self.cumsum_w[end] + 1)
            if picked <= self.cumsum_w[mid]:
                end = mid
            else:
                start = mid + 1
        return start - 1

if __name__ == '__main__':
    from collections import Counter
    c = Counter()
    s = Solution([1, 2, 3, 2])
    N = 1000000
    for i in range(N):
        idx = s.pickIndex()
        c[idx] += 1
    
    for k, v in c.items():
        print(f"{k}: {v / N}")



