from bisect import bisect_left, bisect_right


# --------------------------------
# Solution1 : 运行时间击败了5.57%的用户
class Solution1:
    def insert(self, intervals, newInterval):
        ans = [interval for interval in intervals]
        idx = bisect_left([interval[0] for interval in ans], newInterval[0])
        ans.insert(idx, newInterval)
        
        i = 0
        iterated = 0
        while iterated < len(intervals):
            if ans[i + 1][0] <= ans[i][1]:
                ans[i] = [ans[i][0], max(ans[i][1], ans[i + 1][1])]
                ans.pop(i + 1)
            else:
                i += 1
            iterated += 1
        return ans


# --------------------------------
# Solution2 : 运行时间击败了5.57%的用户
# 上一个解法的冗余： 只需要查看插入位置附近的区间

class Solution:
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        
        idx = bisect_right([interval[0] for interval in intervals], newInterval[0])
        ans = intervals[:idx]
        
        for interval in [newInterval] + intervals[idx:]:
            if not ans or interval[0] > ans[-1][1]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        
        return ans
    

if __name__ == '__main__':
    s = Solution()
    ans = s.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8])
    print(ans, ans == [[1, 2], [3, 10], [12, 16]])
    
    ans = s.insert(intervals=[[1, 5]], newInterval=[1, 7])
    print(ans, ans == [[1, 7]])
    
    ans = s.insert(intervals=[[1, 2], [3, 6]], newInterval=[3, 7])
    print(ans, ans == [[1, 2], [3, 7]])
    
    ans = s.insert(intervals=[[1, 2], [3, 6]], newInterval=[7, 8])
    print(ans, ans == [[1, 2], [3, 6], [7, 8]])

