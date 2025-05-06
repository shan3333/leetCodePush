class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        l = len(s)
        def is_palindrome(word):
            return word == word[::-1]
        
        def dfs(start_index, path):
            if start_index==l:
                res.append(path[:])
                return
            
            for end in range(start_index+1, l+1):
                prefix = s[start_index:end]
                if is_palindrome(prefix):
                    path.append(prefix)
                    dfs(end, path)
                    path.pop()

        dfs(0, [])
        return res
        