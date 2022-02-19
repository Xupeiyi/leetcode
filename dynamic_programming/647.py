# 最终结果不一定直接由dp表格给出
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        is_palindrome = [[1 if i >= j else 0 for j in range(n)] for i in range(n)]
        res = 0
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    is_palindrome[i][j] = is_palindrome[i + 1][j - 1]
                    if is_palindrome[i][j]:
                        res += 1
        return res + len(s)
        
        
if __name__ == '__main__':
    s = Solution()
    ans = s.countSubstrings("lcubxppcmlirhummr")
    print(ans)
    