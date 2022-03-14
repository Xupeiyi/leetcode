from typing import List

def ordered(seq):
    return seq[0] <= seq[-1]


# 思路：target为最小值。 最小值有何特点？ 最小值左边区域有序， 最小值右边区域（包括自身）也有序
# 得到mid后， 可能mid一边有序，另一边无序 => target在无序的那一边
# 在无序的那边寻找target，直到mid左右两边都有序
class Solution:
    def findMin(self, nums: List[int]) -> int:

        start, end = 0, len(nums)-1
        while start <= end:
            if start == end:
                return nums[start]

            mid = (start + end) // 2
            if ordered(nums[start: mid+1]) and ordered(nums[mid+1: end+1]):
                return min(nums[start], nums[mid+1])
            elif ordered(nums[start: mid+1]) and not ordered(nums[mid+1: end+1]):
                start = mid + 1
            elif not ordered(nums[start: mid+1]) and ordered(nums[mid+1: end+1]):
                end = mid
            else:
                return


if __name__ == '__main__':
    s = Solution()
    ans = s.findMin([7, 8, 1, 2, 3, 4, 5, 6])
    print(ans == 1)
    ans = s.findMin([7, 1, 2, 3, 4, 5, 6])
    print(ans == 1)
    ans = s.findMin([1, 2, 3, 4, 5, 6])
    print(ans == 1)
    ans = s.findMin([4, 5, 6, 1, 2, 3])
    print(ans == 1)
    ans = s.findMin([1, 2])
    print(ans == 1)