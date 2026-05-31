1class Solution:
2    def maxProfit(self, prices: List[int], fee: int) -> int:
3        hold = -prices[0]
4        not_hold = 0
5
6        for v in prices[1:]:
7            hold = max(hold, not_hold - v)
8            not_hold = max(hold + v - fee, not_hold)
9        
10        return not_hold