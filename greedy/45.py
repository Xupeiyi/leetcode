class Solution:
    def jump(self, nums):
        length = len(nums)
        count = 0
        
        if length == 1:
            return count
        
        pos = 0
        furthest_reach = nums[0]
        while furthest_reach < length - 1:
            
            start = pos + 1
            end = furthest_reach + 1
            next_pos = start
            
            for i in range(start, end):
                reach = i + nums[i]
                
                if reach >= length - 1:
                    next_pos = i
                    furthest_reach = reach
                    break
                    
                if reach > furthest_reach:
                    next_pos = i
                    furthest_reach = reach
            
            pos = next_pos
            count += 1
            
        return count + 1


if __name__ == '__main__':
    s = Solution()
    ans = s.jump([2, 3, 1, 1, 4])
    print(ans)
    
    ans = s.jump([2, 1])
    print(ans)
    
    ans = s.jump([2, 3, 1])
    print(ans)
    
    ans = s.jump([2, 3, 0, 1, 4])
    print(ans)