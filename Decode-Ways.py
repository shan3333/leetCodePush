class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)

        def is_valid(substring):
            return substring[0] != \0\ and 1 <= int(substring) <= 26

        @lru_cache(maxsize=None)
        def dfs(start):
            if start == l:
                return 1
            total = 0
            for end in range(start+1, min(l+1, start+3)):
                if is_valid(s[start:end]):
                    total += dfs(end)
            return total

        return dfs(0)
        