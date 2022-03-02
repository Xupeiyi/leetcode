class Solution:
    def trailingZeroes(self, n: int) -> int:
        return n // 5 + self.trailingZeroes(n//5) if n else 0


if __name__ == '__main__':
    s = Solution()
    ans = s.trailingZeroes(50)
    print(ans)