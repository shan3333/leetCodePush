class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        charSet = set()
        left = 0

        for right in range(left, len(s)):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxL = max(maxL, len(charSet))
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        return maxL