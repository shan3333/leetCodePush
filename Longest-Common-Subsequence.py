1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        l_1 = len(text1)
4        l_2 = len(text2)
5        dp = {}
6
7        def DP(i: int, j: int) -> int: 
8            if i < 0 or j < 0:
9                return 0
10                
11            if (i,j) in dp:
12                return dp[(i,j)]
13
14            if text1[i] == text2[j]:
15                dp[(i,j)] = DP(i-1, j-1) + 1
16
17            else:
18                dp[(i,j)] = max(DP(i-1, j), DP(i, j-1))
19            return dp[(i,j)]
20
21        return DP(l_1 - 1, l_2 - 1)