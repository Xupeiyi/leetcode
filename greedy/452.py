# first try:
# less efficient
class Solution1:
    def findMinArrowShots(self, points) -> int:
        points = sorted(points, key=lambda x: (x[0], x[1]))
        right_boundary = points[0][1]
        arrows = 1
        for point in points[1:]:
            if point[0] < right_boundary:
                right_boundary = min(point[1], right_boundary)
            else:
                arrows += 1
                right_boundary = point[1]
        
        return arrows
        
        
# more efficient
class Solution:
    def findMinArrowShots(self, points) -> int:
        points.sort(key=lambda x: x[1])
        n = len(points)
        end = points[0][1]
        count = 1
        for i in range(1,n):
            start = points[i][0]
            if start > end:
                count += 1
                end = points[i][1]
        return count