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
 

 # 2022-06-06
class Solution3:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        dp = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1

        longest = s[0]
        longest_length = 1
        for k in range(2, length+1):
            for i in range(length - k + 1):
                j = i + k - 1
                if dp[i+1][j-1] == -1:
                    dp[i][j] = -1
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1] + 2
                        if dp[i][j] > longest_length:
                            longest = s[i: j+1]
                            longest_length = dp[i][j]
                    else:
                        dp[i][j] = -1
        return longest


# -------------------------------------------------
# Solution2

def expand(s, start, end):
    while start >= 0 and end <= len(s) - 1 and s[start] == s[end]:
        start -= 1
        end += 1
        
    return start + 1, end - 1


class Solution2:

    def longestPalindrome(self, s: str):
        start, end = 0, 0
        for i in range(0, len(s)):
            start1, end1 = expand(s, i, i)
            start2, end2 = expand(s, i, i+1)
            
            start, end = max([(start, end), (start1, end1), (start2, end2)],
                             key=lambda x: x[1] - x[0])
        return s[start:end+1]


if __name__ == '__main__':
    s = Solution2()
    ans = s.longestPalindrome("dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
    print(len(ans))
    
    
    