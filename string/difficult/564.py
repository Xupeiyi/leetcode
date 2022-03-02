class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        candidates = [10**(length-1)-1, 10**length+1]  # 本题最tricky的地方
        prefix = int(n[:(length+1) // 2])
        for x in range(prefix-1, prefix+2):
            y = str(x)[:length//2] 
            candidates.append(int(str(x) + str(y)[::-1]))
        num = int(n)
        ans = min([c for c in candidates if c != num], key=lambda x: (abs(x - num), x))
        return str(ans)


if __name__ == '__main__':
    s = Solution()
    ans = s.nearestPalindromic("2")
    print(ans)