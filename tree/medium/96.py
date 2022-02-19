def countTrees(idx, value_range):
    if not value_range:
        return 1
    
    length = len(value_range)
    
    lefts = 0
    for i in range(idx):
        lefts += countTrees(i, value_range[:idx])
    lefts = lefts if lefts else 1
    
    rights = 0
    for i in range(length - idx - 1):
        rights += countTrees(i, value_range[idx + 1:])
    rights = rights if rights else 1
    
    return lefts * rights


class Solution:
    def numTrees(self, n: int):
        ans = 0
        values = [i + 1 for i in range(n)]
        for i in range(n):
            ans += countTrees(i, values)
        return ans


if __name__ == '__main__':
    s = Solution()
    ans = s.numTrees(19)
    print(ans)