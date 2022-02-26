def at_first(nums, n):
    return n > nums[-1]


def at_second(nums, n):
    return n <= nums[-1]


# 初见解法：分类讨论。将被旋转的数组分为两个区域（称为左，右）， 
# 然后分类讨论mid在左半边， target在左半边...等等， 决定下一步在
# mid左边或右边继续搜索
class Solution1:
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


# 将数组一分为二，其中一定有一个是有序的，另一个可能是有序，也能是部分有序。
# 此时有序部分用二分法查找。无序部分再一分为二，其中一个一定有序，另一个可能有序，可能无序。就这样循环. 
class Solution:
    
    def search(self, nums, target) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            
            # 左半边有序
            if nums[0] <= nums[mid]:
                # target在左半边
                if nums[0] <= target < nums[mid]:
                    end = mid - 1
                # 去右半边查找
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
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
