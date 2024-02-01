# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(left, right, root):
            if not root:
                return True
            if not ( root.val > left and root.val < right):
                return False
            return validate(left, root.val, root.left) and validate(root.val, right, root.right)
        
        return validate(float('-inf'), float('inf'), root)