class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[1])
        
        count = 0
        end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] >= end:
                end = interval[1]
            else:
                count += 1
        
        return count