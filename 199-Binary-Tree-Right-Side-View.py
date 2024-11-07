# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        list = []

        def dfs(node, level):
            if not node:
                return
            if len(list) < level:
                list.append(node.val)
            dfs(node.right, level+1)
            dfs(node.left, level+1)

            return

        dfs(root, 1)
        return list
                    