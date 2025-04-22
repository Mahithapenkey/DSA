# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(leftroot,rightroot):
            if not leftroot and not rightroot:
                return True
            if not leftroot or not rightroot or leftroot.val!=rightroot.val:
                return False
            
            c1= leftroot.val == rightroot.val
            c2=mirror(leftroot.left,rightroot.right)
            c3=mirror(leftroot.right,rightroot.left)
            return c1 and c2 and c3
        return mirror(root.left,root.right)
            

        

        