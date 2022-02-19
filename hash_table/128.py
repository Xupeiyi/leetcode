# Solution 1
class Solution1:
    def longestConsecutive(self, nums) -> int:
        visited_idx = set()
        num_pos = {n: i for i, n in enumerate(nums)}
        max_length = 0
        
        for num in nums:
            
            if num_pos[num] in visited_idx:
                continue
            
            length = 1
            n = num + 1
            while n in num_pos.keys() and num_pos[n] not in visited_idx:
                visited_idx.add(num_pos[n])
                n += 1
                length += 1
            
            n = num - 1
            while n in num_pos.keys() and num_pos[n] not in visited_idx:
                visited_idx.add(num_pos[n])
                n -= 1
                length += 1
            
            max_length = max(length, max_length)
        
        return max_length


# Solution 2:
# 只从最小的数开始计算长度即可
class Solution:
    def longestConsecutive(self, nums) -> int:
        num_set = set(nums)
        max_length = 0
        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                n = num + 1
                while n in num_set:
                    length += 1
                    n += 1
                max_length = max(length, max_length)
        
        return max_length
        

if __name__ == '__main__':
    s = Solution()
    ans = s.longestConsecutive([100, 4, 5, 200, 1, 3, 2])
    print(ans == 5)
    
    ans = s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
    print(ans == 9)
