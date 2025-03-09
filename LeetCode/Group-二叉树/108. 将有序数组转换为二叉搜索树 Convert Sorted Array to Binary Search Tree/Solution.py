# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
二叉搜索树是一种二叉树，其中每个节点都满足以下条件：

1. 左子树中的所有节点的值都小于当前节点的值。

2. 右子树中的所有节点的值都大于当前节点的值。

3. 左子树和右子树也分别是二叉搜索树。

因此写一个递归体用来创建树，由于是升序数列：

如果插入值小于当前节点的值，递归创建左子树。
如果插入值大于当前节点的值，递归创建右子树。
插入值就是中间的数，因为它比左边的大，比右边的小，所以用来做当前的根节点返回
"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def insertor(left_index, right_index):
            if left_index > right_index:
                return None
            mid_index = (left_index + right_index) // 2
            root_node = TreeNode(nums[mid_index])
            root_node.left = insertor(left_index, mid_index - 1)
            root_node.right = insertor(mid_index + 1, right_index)
            return root_node
        return insertor(0, len(nums) - 1)