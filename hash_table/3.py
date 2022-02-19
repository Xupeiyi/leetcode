class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = {}
        length = 0
        start = 0
        for i, char in enumerate(s):
            
            if char in pos.keys():
                length = max(i - start, length)
                
                # drop all positions between [start, pos[char])
                for idx in range(start, pos[char]):
                    pos.pop(s[idx])
                
                # update start position
                start = pos[char] + 1
                pos[char] = i
            
            else:
                pos[char] = i
        
        return max(length, len(s) - start)


if __name__ == '__main__':
    s = Solution()
    ans = s.lengthOfLongestSubstring("pwwkew")
    print(ans)