from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        
        for s in strs:
            anagrams[tuple(sorted(s))].append(s)
        
        return list(anagrams.values())


if __name__ == '__main__':
    s = Solution()
    ans = s.groupAnagrams(["a"])
    print(ans)