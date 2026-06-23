1class Solution:
2    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
3        intervals.sort(key=lambda l:l[1])
4        ans = 0
5        start = intervals[0][0]
6        end = intervals[0][1]
7        for i in range(1, len(intervals)):
8            new_start = intervals[i][0]
9            new_end = intervals[i][1]
10            if new_start < end:
11                ans += 1
12            else:
13                end = new_end
14
15        return ans