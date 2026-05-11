1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        prev1 = 0
4        prev2 = 0
5
6        for num in nums:
7            cur = max(prev2 + num, prev1)
8            prev2 = prev1
9            prev1 = cur
10
11        return max(prev1, prev2)
12
13        