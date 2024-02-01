# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getHeight(root):
            if not root:
                return -1
            left = getHeight(root.left)
            right = getHeight(root.right)
            return 1 + max(left, right)
        res = [0]
        def getDiameter(root):
            if not root:
                return 0
            left = getHeight(root.left)
            right = getHeight(root.right)
            res[0] = max(res[0], 2 + left + right)
            getDiameter(root.left)
            getDiameter(root.right)
            return 
        getDiameter(root)
        return res[0]