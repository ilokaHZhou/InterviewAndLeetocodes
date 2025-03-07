"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # 原节点 -> 新节点映射
        mapping = {}

        # 第一次遍历：创建所有节点并存储在哈希表中
        curr = head
        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next
        
        # 第二次遍历：设置新节点的 next 和 random 指针
        curr = head
        while curr:
            clone = mapping.get(curr)
            clone.next = mapping.get(curr.next)
            clone.random = mapping.get(curr.random)
            curr = curr.next

        # 返回新的链表的头节点,此时头节点已经指向新创建的链表
        return mapping.get(head)