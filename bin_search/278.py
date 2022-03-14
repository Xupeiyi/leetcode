class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start <= end:
            mid = (start + end) // 2

            if isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1
        
        return start