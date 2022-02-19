class Solution:
    def singleNumber(self, nums) -> int:
        a = 0
        for n in nums:
            a ^= n
        return a

if __name__ == '__main__':
    print(Solution().singleNumber([2, 4, 1, 1, 2]))