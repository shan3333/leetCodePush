class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(int)
        l = deque()
        ans = 1

        if s == "":
            return 0

        for i in s:
            d[i] += 1
            l.append(i)
            while d[i]>1:
                ans = max(ans, len(l)-1)
                d[l.popleft()] -= 1
        
        ans = max(ans, len(l))
              
        return ans

            