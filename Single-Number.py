1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        c = 0
4        for i in nums:
5            c = c ^ i
6        
7        return c