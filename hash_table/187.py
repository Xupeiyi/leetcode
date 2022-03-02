from typing import List
from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counter = defaultdict(int)
        for i in range(len(s)-9):
            counter[s[i:i+10]] += 1
        return list(s for s, c in counter.items() if c > 1)

if __name__ == '__main__':
    s = Solution()
    ans = s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCAAAAATTGGCC")
    print(ans)