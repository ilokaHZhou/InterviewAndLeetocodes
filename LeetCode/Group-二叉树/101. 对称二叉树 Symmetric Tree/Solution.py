# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(left, right):  # 判断两棵树是否镜像对称
            if not left and not right:  # 如果两个节点都为空
                return True
            if not left or not right:  # 如果只有一个节点为空
                return False
            # 检查当前节点值是否相等，并递归检查左右子树
            return (left.val == right.val and
                    is_mirror(left.left, right.right) and
                    is_mirror(left.right, right.left))

        if not root:  # 如果根节点为空
            return True
        return is_mirror(root.left, root.right)  # 检查左右子树是否镜像对称