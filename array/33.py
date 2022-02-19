def at_first(nums, n):
    return n > nums[-1]


def at_second(nums, n):
    return n <= nums[-1]


class Solution:
    def search(self, nums, target) -> int:
        
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            nmid = nums[mid]
            
            if nmid == target:
                return mid
            elif (at_first(nums, target) and at_first(nums, nmid) and target < nmid) \
                    or (at_second(nums, target) and at_second(nums, nmid) and target < nmid) \
                    or (at_first(nums, target) and at_second(nums, nmid)):
                end = mid - 1
            
            else:
                start = mid + 1
        
        return -1


if __name__ == '__main__':
    s = Solution()
    ans = s.search([4, 5, 6, 7, 1, 2, 3], 5)
    print(ans == 1)
    ans = s.search([4, 5, 6, 7, 1, 2, 3], 4)
    print(ans == 0)
    ans = s.search([4, 5, 6, 7, 1, 2, 3], 7)
    print(ans == 3)
    
    ans = s.search([4, 5, 6, 7, 1, 2, 3], 1)
    print(ans == 4)
    ans = s.search([4, 5, 6, 7, 1, 2, 3], 2)
    print(ans == 5)
    ans = s.search([4, 5, 6, 7, 1, 2, 3], 3)
    print(ans == 6)
    
    ans = s.search([4, 5, 6, 7, 0, 1, 2], 3)
    print(ans == -1)
    
    ans = s.search([1], 0)
    print(ans == -1)
