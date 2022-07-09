from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [1 for _ in range(n)]
        ptrs = [0 for _ in primes]

        for i in range(1, n):
            dp[i] = min(dp[ptr] * prime for ptr, prime in zip(ptrs, primes))
            
            for j, prime in enumerate(primes):
                if dp[ptrs[j]] * prime == dp[i]:
                    ptrs[j] += 1
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    ans = s.nthSuperUglyNumber(12, [2, 7, 13, 19])
    print(ans)