class Solution:
    def reverseBits(self, n):
        rev = 0
        i = 0
        while i < 32 and n != 0:
            #     取最后一位  左移
            rev |= (n & 1) << (31 - i)
            n = n >> 1
            i += 1
        return rev


if __name__ == '__main__':
    s = Solution()
    ans = s.reverseBits(43261596)
    print(ans)