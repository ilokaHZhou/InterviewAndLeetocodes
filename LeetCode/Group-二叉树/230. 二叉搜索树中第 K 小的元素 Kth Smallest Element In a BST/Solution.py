# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
由于中序遍历就是在从小到大遍历节点值，所以遍历到的第 k 个节点值就是答案。
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def traverse(node):
            if not node:
                return -1

            # 递归遍历左子树
            left_check = traverse(node.left)
            # 这里是为了在左子树中找到第 k 小的元素时提前返回，避免不必要的遍历
            if left_check != -1:
                return left_check
            
            # 检测当前node的值是否是第k个值，由于需要更新k，因此不能直接用外层作用域的k，前面要加nonlocal
            # k = k - 1是因为每查看过一个节点就需要减一，直到k=0，无论左右,由于是中序遍历，一定是从小到大依次检查
            nonlocal k
            k = k - 1
            if k == 0:
                return node.val

            # 由于右侧遍历前就会检查node的值是否是第k个，已经确保了左子树和当前节点都没有找到，因此不需要像左节点一样if check
            return traverse(node.right)
        return traverse(root)
