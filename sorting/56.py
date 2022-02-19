class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])
        ans = [intervals[0]]

        for interval in intervals[1:]:
            if interval[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], interval[1])
            else:
                ans.append(interval)
        
        return ans


if __name__ == '__main__':
    s = Solution()
    input_ = [[1,4],[4,5]]
    ans = s.merge(input_)
    print(ans)
