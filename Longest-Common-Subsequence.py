1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        i, j = 0, 0
4        l_1 = len(text1)
5        l_2 = len(text2)
6        dp = [[0] * (l_2 + 1) for _ in range(l_1 + 1)]
7
8        for i in range(1, l_1 + 1):
9            for j in range(1, l_2 + 1):                    
10                if text1[i-1] == text2[j-1]:
11                    dp[i][j] = dp[i-1][j-1] + 1
12                else:
13                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
14            
15        return dp[l_1][l_2]
16            