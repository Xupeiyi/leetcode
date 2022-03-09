# 去掉非质数的比选择质数更快
class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [1] * n

        i = 2
        while i*i < n:
            if is_prime[i]:
                j = i*i
                while j < n:
                    is_prime[j] = 0
                    j += i
            i += 1
        return sum(is_prime[2:])

if __name__ == '__main__':
    s = Solution()
    ans = s.countPrimes(20)
    print(ans)