class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'()', '[]', '{}'}

        for i in s:
            if i in '([{':
                stack.append(i)
            elif not stack or stack.pop() + i not in dic:
                return False
            
        return not stack
            
