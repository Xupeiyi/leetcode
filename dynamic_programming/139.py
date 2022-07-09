class Solution1:
    def wordBreak(self, s: str, wordDict) -> bool:
        dp = [True] + [False]*len(s)
        
        wordSet = set(wordDict)
        min_len = min([len(w) for w in wordDict])

        for i in range(min_len, len(s)+1):
            for j in range(0, i):
                if s[j:i] in wordSet and dp[j]:
                    dp[i] = True

        return dp[-1]

class Solution2:
    def wordBreak(self, s: str, wordDict) -> bool:
        dp = [True] + [False]*len(s)
        
        min_len = min([len(w) for w in wordDict])

        for i in range(min_len, len(s)+1):
            for word in wordDict:
                if s[:i].find(word, i-len(word)) != -1 and dp[i-len(word)]:
                    dp[i] = True

        return dp[-1]
    
    
# 2022-06-16
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for i in range(1, len(s) + 1):
            for word in wordDict:
                length = len(word)
                if i < length:
                    continue
                if s[i-length: i] == word and dp[i-length] == True:
                    dp[i] = True
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    ans = s.wordBreak("leetcode", ["leet", "code"])
    print(ans)
    
    ans = s.wordBreak("applepenapple", ["pen", "apple"])
    print(ans)
    
    ans = s.wordBreak("catsandog", ["cat", "cats", "dog", "sand", "and"])
    print(ans)
    
    ans = s.wordBreak("bb", ["a", "b"])
    print(ans)
    
    ans = s.wordBreak("aaaaaaa", ["aaa", "aaaa"])
    print(ans)