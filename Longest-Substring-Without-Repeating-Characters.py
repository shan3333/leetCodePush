class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        m = 0
        d: dict(str, int) = defaultdict(int)
        
        for r in range(len(s)):
            d[s[r]] += 1
            while d[s[r]] > 1:
                d[s[l]] -= 1
                l += 1
            m = max(m, r-l+1)
        return m