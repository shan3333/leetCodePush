1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        s = set()
4        for i in nums:
5            if i not in s:
6                s.add(i)
7            else:
8                s.remove(i)
9        
10        return s.pop()