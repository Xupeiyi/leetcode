from itertools import cycle


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        dist = 2 * (numRows-1)
        ans = []
        for i in range(numRows):
            ans.append(s[i])
            steps = cycle([x for x in (dist-2*i, 2*i) if x != 0])
            curr = i + next(steps)
            while curr < len(s):
                ans.append(s[curr])
                curr += next(steps)
                
        return "".join(ans)
    
    
if __name__ == '__main__':
    s = Solution()
    ans = s.convert("PAYPALISHIRING", 5)
    print(ans)