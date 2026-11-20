# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        que = deque([root])
        while que:
            q = que.popleft()
            q.left, q.right = q.right, q.left
            if q.left:
                que.append(q.left)
            if q.right:
                que.append(q.right)
        return root