class TreeNode:
    def __init__(self, x):
        self.val = x  # 节点的值
        self.left = None  # 左子节点
        self.right = None  # 右子节点

def build_tree(preorder, inorder):
    # 根据前序和中序遍历结果构造二叉树
    if not preorder or not inorder:
        return None
    # 前序遍历的第一个值是根节点
    root = TreeNode(preorder[0])
    # 在中序遍历中找到根节点的索引
    mid = inorder.index(preorder[0])
    # 递归构造左子树和右子树
    root.left = build_tree(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree(preorder[mid+1:], inorder[mid+1:])
    return root

def update_tree(node):
    # 更新节点值为其所有子节点的和
    if not node:
        return 0
    left_sum = update_tree(node.left)
    right_sum = update_tree(node.right)
    old_val = node.val
    node.val = left_sum + right_sum
    return node.val + old_val

def inorder_traversal(node):
    # 中序遍历
    if not node:
        return []
    return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

if __name__ == '__main__':
    # 输入中序和前序遍历的结果
    inorder = list(map(int, input().split()))
    preorder = list(map(int, input().split()))
    # 构造二叉树
    root = build_tree(preorder, inorder)
    # 更新二叉树的节点值
    update_tree(root)
    # 进行中序遍历并打印结果
    print(' '.join(map(str, inorder_traversal(root))))