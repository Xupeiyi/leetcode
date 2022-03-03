from typing import List


# 第一次接触单调栈
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        # min_left, min_stack 记录nums[i]左边离它最近并比它小的元素
        # max_left, max_stack 记录nums[i]左边离它最近并比它大的元素
        min_left, max_left = [0] * n, [0] * n 
        min_stack, max_stack = [], [] 
        for i, num in enumerate(nums): 
            while min_stack and nums[min_stack[-1]] > num:
                min_stack.pop()
            min_left[i] = min_stack[-1] if min_stack else -1
            min_stack.append(i)

            # nums[i]和栈顶元素值相等时， 认为下标大的元素更大
            while max_stack and nums[max_stack[-1]] <= num: 
                max_stack.pop()
            max_left[i] = max_stack[-1] if max_stack else -1
            max_stack.append(i)


        min_right, max_right = [0] * n, [0] * n
        min_stack, max_stack = [], []
        for i in range(n-1, -1, -1):
            num = nums[i]
            while min_stack and nums[min_stack[-1]] >= num:
                min_stack.pop()
            min_right[i] = min_stack[-1] if min_stack else n
            min_stack.append(i)

            while max_stack and nums[max_stack[-1]] < num:
                max_stack.pop()
            max_right[i] = max_stack[-1] if max_stack else n
            max_stack.append(i)

        sum_max = sum((max_right[i] - i) * (i - max_left[i]) * nums[i]
                        for i in range(n))
        sum_min = sum((min_right[i] - i) * (i - min_left[i]) * nums[i]
                        for i in range(n))
        return sum_max - sum_min

if __name__ == '__main__':
    s = Solution()
    ans = s.subArrayRanges([1, 3, 3])
    print(ans)