from typing import List
from functools import cmp_to_key

def compare(s1, s2):
    # 刚开始的想法。想得太复杂了。
    # 想通过挨个比较每一位数字的方法确定顺序，比如 '95' > '92'
    # 这样很难处理 s1=432, s2=43243 或者 s1=1113,s2=111311 之类的情况 
    # n1 = len(s1)
    # n2 = len(s2)

    # i = 0
    # while i < n1 and i < n2:
    #     digit1 = int(s1[i])
    #     digit2 = int(s2[i])

    #     if digit1 > digit2:
    #         return 1
    #     elif digit1 < digit2:
    #         return -1
    #     i += 1
    # if n1 > n2:
    #     return 1 if s1[i] >= s1[0] else -1
    # elif n1 < n2:
    #     return -1 if s2[i] >= s2[0] else 1


    if int(s1 + s2) > int(s2 + s1):
        return 1
    elif int(s1 + s2) < int(s2 + s1):
        return -1
    
    return 0


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if all([n == 0 for n in nums]):
            return '0'
        strs = [str(n) for n in nums]
        order = sorted(strs, key=cmp_to_key(compare), reverse=True)
        return ''.join(order)


if __name__ == '__main__':
    s = Solution()
    ans = s.largestNumber([432, 43243])
    print(ans)