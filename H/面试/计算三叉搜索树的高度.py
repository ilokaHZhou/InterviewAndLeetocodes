class TreeNode:
    def __init__(self, val):
        self.val = val  # 节点值
        self.left = self.mid = self.right = None  # 左、中、右子节点

class Tree:
    # 插入方法：向树中插入值
    def insert(self, root, val):
        if root is None:
            return TreeNode(val)  # 如果根节点为空，创建新节点作为根节点
        if val < root.val - 500:
            root.left = self.insert(root.left, val)  # 如果值小于根节点值减500，插入到左子树
        elif val > root.val + 500:
            root.right = self.insert(root.right, val)  # 如果值大于根节点值加500，插入到右子树
        else:
            root.mid = self.insert(root.mid, val)  # 如果值在根节点值加减500范围内，插入到中间子树
        return root  # 返回根节点

    # 获取树的高度
    def get_height(self, root):
        if root is None:
            return 0  # 如果根节点为空，高度为0
        left_height = self.get_height(root.left)  # 计算左子树的高度
        mid_height = self.get_height(root.mid)  # 计算中间子树的高度
        right_height = self.get_height(root.right)  # 计算右子树的高度
        return max(left_height, mid_height, right_height) + 1  # 返回三者中最大的高度加1

if __name__ == '__main__':
    tree = Tree()  # 创建树对象
    N = int(input())  # 读取节点数量
    root = None  # 初始化根节点为None
    nums = list(map(int, input().split()))
    for num in nums:
        root = tree.insert(root, num)  # 将每个整数插入树中     
    height = tree.get_height(root)  # 获取树的高度
    print(height)  # 输出树的高度