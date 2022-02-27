class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        letters = set([str(i) for i in range(1, 27)] + [''])
        nums = [1] * (len(s) + 1) 

        for i in range(1, len(s)):
            res = 0
            if s[i] != '0':
                res += nums[i]
            
            if s[i-1: i+1] in letters:
                res += nums[i-1]
            nums[i+1] = res
        return nums[-1]

if __name__ == '__main__':
    s = Solution()
    ans = s.numDecodings('226')
    print(ans)