def digits(n):
    d = []
    while n:
        d.append(n % 10)
        n = n // 10
    return d


class Solution:
    def isHappy(self, n: int) -> bool:
        squares = {n: n**2 for n in range(0, 10)}
        results = set()
        while True:
            res = sum(squares[i] for i in digits(n))
            if res in results:
                return False
            results.add(res)
            n = res
            if res == 1:
                break
            
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(19))