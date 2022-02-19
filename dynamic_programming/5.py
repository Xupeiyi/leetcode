# --------------------------------------------
# Solution1


class Solution1:
    def longestPalindrome(self, s: str):
        p_start = 0
        p_length = 1
        dp = [[False] * len(s) for _ in s]
        
        for length in range(1, len(s)+1):
            for start in range(0, len(s)):
                end = start + length - 1
                if end > len(s) - 1:
                    break
                    
                if s[start] != s[end]:
                    dp[start][end] = False
                else:
                    dp[start][end] = dp[start+1][end-1] if length > 2 else True
                
                if dp[start][end] and length > p_length:
                    p_start = start
                    p_length = length

        return s[p_start:p_start + p_length]
 

# -------------------------------------------------
# Solution2

def expand(s, start, end):
    while start >= 0 and end <= len(s) - 1 and s[start] == s[end]:
        start -= 1
        end += 1
        
    return start + 1, end - 1


class Solution:

    def longestPalindrome(self, s: str):
        start, end = 0, 0
        for i in range(0, len(s)):
            start1, end1 = expand(s, i, i)
            start2, end2 = expand(s, i, i+1)
            
            start, end = max([(start, end), (start1, end1), (start2, end2)],
                             key=lambda x: x[1] - x[0])
        return s[start:end+1]


if __name__ == '__main__':
    s = Solution()
    ans = s.longestPalindrome("dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
    print(len(ans))
    
    
    