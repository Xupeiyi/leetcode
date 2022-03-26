def get_steps(cur: int, n: int) -> int:
    """returns the correct answer only when cur >= 10"""
    steps, first, last = 0, cur, cur
    while first <= n:
        steps += min(last, n) - first + 1
        first *= 10
        last = last * 10 + 9
    return steps


class Solution:
    def findKthNumber(self, n, k):
        cur = 1
        k -= 1
        while k:
            steps = get_steps(cur, n)

            if steps <= k:
                k -= steps
                cur += 1
            else:
                cur *= 10
                k -= 1
        return cur


if __name__ == '__main__':
    s = Solution()
    ans = s.findKthNumber(106, 4)
    print(ans)