def insort(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]:
            hi = mid
        elif x > a[mid]:
            lo = mid+1
        else:
            return
    a.insert(lo, x)


class Solution:
    def lastStoneWeightII(self, stones) -> int:
        sum_stones = sum(stones)
        target = sum_stones // 2
        sums = [0]
        sums_set = {0}
        
        for st in sorted(stones):
            tmp = []
            for sum_ in sums:
                new_sum = st + sum_
                if new_sum < target:
                    tmp.append(new_sum)
                elif new_sum == target:
                    return sum_stones - target*2
                else:
                    break
            
            for t in tmp:
                insort(sums, t)
        
        return sum_stones - sums[-1]*2


if __name__ == '__main__':
    s = Solution()
    ans = s.lastStoneWeightII([31, 26, 33, 21, 40])
    print(ans)