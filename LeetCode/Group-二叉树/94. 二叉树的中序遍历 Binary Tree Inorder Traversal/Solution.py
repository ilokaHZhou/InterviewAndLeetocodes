# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
1. 递归，中序遍历按照左根右遍历
注：使用 nonlocal result可以直接获取外层result数组，这样可以不用把result传进递归体

2. 栈实现非递归遍历，将左节点依次加入栈stk，当左节点为空时，弹出空节点，加入根节点，然后选择右节点继续找其下面的左节点
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans, stk = [], []
        while root or stk:
            if root:
                stk.append(root)
                root = root.left
            else:
                root = stk.pop()
                ans.append(root.val)
                root = root.right
        return ans
"""
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, result):
            if root is None:
                return
            dfs(root.left, result)
            result.append(root.val)
            dfs(root.right, result)

        result = []
        dfs(root, result)
        return result