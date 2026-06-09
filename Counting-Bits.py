1class Solution:
2    def countBits(self, n: int) -> List[int]:
3        ans = [0] * (n + 1)
4        for i in range(n + 1):
5            ans[i] = ans[i >> 1] + (i & 1)
6        return ans