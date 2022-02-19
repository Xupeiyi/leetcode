class Solution:
    def partitionLabels(self, s: str):
        intervals = dict()
        
        for i, char in enumerate(s):
            interval = intervals.get(char, [i, i])
            intervals[char] = [interval[0], i]
        
        intervals = sorted(list(intervals.values()), key=lambda x: x[0])
        intervals.append([len(s), len(s)])
        
        ans = []
        start = intervals[0][0]
        end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] > end:
                ans.append(interval[0]-start)
                start = interval[0]
                end = interval[1]
            else:
                end = max(end, interval[1])
        
        return ans
        

if __name__ == '__main__':
    s = Solution()
    res = s.partitionLabels("ababcbacadefegdehijhklij")
    print(res)