1class Solution:
2    def findMinArrowShots(self, points: List[List[int]]) -> int:
3        points.sort(key=lambda p:p[1])
4        l = len(points)
5        overlap = 0
6        start = points[0][0]
7        end = points[0][1]
8        for i in range(1, l):
9            new_start = points[i][0]
10            new_end = points[i][1]
11            if new_start <= end:
12                overlap += 1
13            else:
14                end = new_end
15        
16        return l - overlap