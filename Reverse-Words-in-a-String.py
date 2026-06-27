1class Solution:
2    def reverseWords(self, s: str) -> str:
3        s_strip = s.strip()
4        s_split = s_strip.split()
5        s_split.reverse()
6        return ' '.join(s_split)