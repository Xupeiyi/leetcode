from typing import List

# 使用原地哈希的做法，虽然违反了不能修改数组的规则
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 数字范围: [1, n]
        # 下标范围: [0, n]
        for n in nums:
            idx = abs(n)
            if nums[idx] < 0:
                return idx
            else:
                nums[idx] *= -1

# 数组也能表示链表
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]  # 相当于fast = fast.next.next 

            if slow == fast:
                break
        
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow