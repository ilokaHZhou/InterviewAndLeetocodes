# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) #遍历每个节点
            right_height = self.maxDepth(root.right) 
            # 最下一层节点作为root子树不能再往下所以深度为0，因此自身为1，以此类推向上2，3...
            return max(left_height, right_height) + 1 
