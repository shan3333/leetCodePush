1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        d_min_cost = {}
4        top_stair = len(cost)
5
6        def dp(index: int) -> int:
7            if index == 0 or index == 1:
8                return 0
9            
10            if index in d_min_cost:
11                return d_min_cost[index]
12
13            cost_to_stair_1 = dp(index - 1) + cost[index - 1]
14            cost_to_stair_2 = dp(index - 2) + cost[index - 2]
15            
16            min_cost = min(cost_to_stair_1, cost_to_stair_2)
17            d_min_cost[index] = min_cost
18
19            return min_cost
20
21        return dp(top_stair)