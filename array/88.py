def at_first(nums, n):
    return n > nums[-1]


def at_second(nums, n):
    return n <= nums[-1]

# 本题与33题的不同在于因为有重复元素，无法判断数字n在第一部分或第二部分。
# 进一步思考，在什么时候无法判断？
# 对 nums = [5, 5, 6, 7, 1, 2, 3, 3], 还是可以判断 n 在哪一部分的
# 对 nums = [5, 5, 6, 7, 1, 2, 5, 5], 可以判断 1 在第二部分， 7 在第一部分，但无法判断5在哪一部分， 因为两边都有5
# 所以应对办法是当 nmid == nums[start] and nmid == nums[end]时， 从两边缩短nums, 直到能够进行判断 
class Solution:
    def search(self, nums, target) -> int:
        
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            nmid = nums[mid]
            
            if nmid == target:
                return True

            if nums[start] == nmid and nmid == nums[end]:
                start += 1
                end -= 1
            elif (at_first(nums[start: end+1], target) and at_first(nums[start: end+1], nmid) and target < nmid) \
                    or (at_second(nums[start: end+1], target) and at_second(nums[start: end+1], nmid) and target < nmid) \
                    or (at_first(nums[start: end+1], target) and at_second(nums[start: end+1], nmid)):
                end = mid - 1
            else:
                start = mid + 1
        
        return False


if __name__ == '__main__':
    s = Solution()
    ans = s.search([1, 0, 1, 1, 1], 0)
    print(ans == True)

