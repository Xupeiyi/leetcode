from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre_max = nums[0]
        pre_min = nums[0]

        res = nums[0]
        for num in nums[1:]:
            a = num * pre_max
            b = num * pre_min
            curr_max = max(num, a, b)
            curr_min = min(num, a, b)
            res = max(res, curr_max)
            pre_max = curr_max
            pre_min = curr_min

        return res

if __name__ == '__main__':
    s = Solution()
    ans = s.maxProduct([1, 2, 3, 4])
    print(ans == 24)

    ans = s.maxProduct([1, -2, 3, -4])
    print(ans == 24)



