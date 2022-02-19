class Solution:
    def findContentChildren(self, g, s):
        g = sorted(g)
        s = sorted(s)
        child = 0
        for cookie in s:
            if child < len(g) and cookie >= g[child]:
                child += 1
        return child
    

if __name__ == '__main__':
    s = Solution()
    ans = s.findContentChildren([1, 2], [1, 2, 3])
    print(ans)