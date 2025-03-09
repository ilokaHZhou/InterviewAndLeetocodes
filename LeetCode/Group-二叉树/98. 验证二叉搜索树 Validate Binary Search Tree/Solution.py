# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, lower, higher):
            # 遇到叶子节点直接返回True
            if not node:
                return True

            # 不是叶子的枝干节点要按照根节点值一定大于左边，小于右边的原则比较，相等也是不行的
            curr_node_val = node.val
            if curr_node_val <= lower or curr_node_val >= higher:
                return False

            # 递归查找左右两颗子树，两边都是True才返回True
            left_check = check(node.left, lower, curr_node_val)
            right_check = check(node.right, curr_node_val, higher)
            return left_check and right_check
        return check(root, float('-inf'), float('inf'))