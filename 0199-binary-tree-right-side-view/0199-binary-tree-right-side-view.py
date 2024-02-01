# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        res = []
        while q:
            rightNode = None
            for i in range(len(q)):
                node = q.popleft()
                if not node:
                    continue
                rightNode = node
                q.append(node.left)
                q.append(node.right)
            if rightNode:
                res.append(rightNode.val)
        return res
            
        