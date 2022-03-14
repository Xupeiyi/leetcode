from typing import List


def bisect_leftmost(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start
        

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        pos = {start: i for i, (start, _) in enumerate(intervals)}
        sorted_starts = sorted([start for start, _ in intervals])
        ans = []
        for _, end in intervals:
            start_idx = bisect_leftmost(sorted_starts, end)
            start = pos[sorted_starts[start_idx]] if start_idx < len(sorted_starts) else -1
            ans.append(start)
        return ans