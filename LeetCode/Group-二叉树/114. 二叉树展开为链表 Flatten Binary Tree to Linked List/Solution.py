# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
1. 前序遍历 空间复杂度O(n)
2. 前驱节点，空间复杂度O(1)：

前序遍历访问各节点的顺序是根节点、左子树、右子树。如果一个节点的左子节点为空，则该节点不需要进行展开操作。如果一个节点的左子节点不为空，则该节点的左子树中的最后一个节点被访问之后，该节点的右子节点被访问。该节点的左子树中最后一个被访问的节点是左子树中的最右边的节点，也是该节点的前驱节点。

    def flatten(self, root: TreeNode) -> None:
        curr = root
        while curr:
            if curr.left:
                # pre和next到当前节点的左节点上
                predecessor = nxt = curr.left

                # pre遍历此左节点的所有右节点
                while predecessor.right:
                    predecessor = predecessor.right
                
                # 把当前节点的右节点摘下来放到pre的末尾，把当前节点的左节点甩到右侧上
                # 这样新树顺序就是node -> node.left -> node.right正是前序顺序
                predecessor.right = curr.right
                curr.left = None
                curr.right = nxt
            curr = curr.right

"""
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        preOderList = []

        # 用前序遍历拿node
        def preOrderTravese(node):
            if node:
                preOderList.append(node)
                preOrderTravese(node.left)
                preOrderTravese(node.right)

        preOrderTravese(root)

        # 创建新链表树
        for i in range(len(preOderList) - 1):
            preOderList[i].left = None
            preOderList[i].right = preOderList[i + 1]