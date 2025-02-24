# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # 创建一个虚拟头节点
        current = dummy  # 当前节点指针

        while list1 and list2:  # 遍历两个链表
            if list1.val < list2.val:  # 如果 list1 的值较小
                current.next = list1  # 将 list1 的节点连接到结果链表
                list1 = list1.next  # 移动 list1 的指针
            else:  # 如果 list2 的值较小
                current.next = list2  # 将 list2 的节点连接到结果链表
                list2 = list2.next  # 移动 list2 的指针
            current = current.next  # 移动当前节点指针

        # 将剩余的链表连接到结果链表
        current.next = list1 if list1 else list2

        return dummy.next  # 返回合并后的链表头节点