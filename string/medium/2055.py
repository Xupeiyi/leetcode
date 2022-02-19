import bisect


def find_min_ge(series, n):
    """找到series中大于等于n的最小的数的位置"""
    idx = bisect.bisect_left(series, n)
    return idx


def find_max_le(series, n):
    """找到series中小于等于n的最大的数的位置"""
    idx = bisect.bisect_right(series, n)
    return idx - 1


class Solution:
    def platesBetweenCandles(self, s: str, queries):
        candles = []
        for i, char in enumerate(s):
            if char == '|':
                candles.append(i)

        ans = []
        for q in queries:
            i = find_min_ge(candles, q[0])
            j = find_max_le(candles, q[1])
            plates = candles[j] - candles[i] - (j - i) if j > i else 0
            ans.append(plates)
        
        return ans


if __name__ == '__main__':
    print(find_min_ge([3, 6, 12, 15, 16, 19], 4))

    print(find_max_le([3, 6, 12, 15, 16, 19], 5))
    
    s = Solution()
    print(s.platesBetweenCandles("***|**|*****|**||**|*", [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]))
