# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(root,dir,zigzag):
            if root is None:
                return 
            self.path = max(self.path,zigzag)
            if dir == 'left':
                dfs(root.left,'left',1)
                dfs(root.right,'right',zigzag+1)
            else:
                dfs(root.left,'left',zigzag+1)
                dfs(root.right,'right',1)
        self.path=0
        dfs(root.right,'right',1)
        dfs(root.left,'left',1)
            
        return self.path