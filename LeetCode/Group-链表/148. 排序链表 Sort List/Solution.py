# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
排序算法	时间复杂度	空间复杂度	适用场景
归并排序	O(n log n)	O(1) 或 O(log n)	链表长度较大时
插入排序	O(n²)	O(1)	链表长度较小或近乎有序时

建议用归并做
"""
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 递归终止条件：链表为空或只有一个节点
        if not head or not head.next:
            return head

        # 找到链表的中间节点
        mid = self.findMiddle(head)
        # 分割链表，因为中间要切断链表mid.next = None，所以先保存右侧头节点
        right_head = mid.next
        mid.next = None  # 切断链表

        # 递归排序左右两部分
        left = self.sortList(head)
        right = self.sortList(right_head)

        # 合并两个有序链表
        return self.mergeTwoLists(left, right)

    def findMiddle(self, head: ListNode) -> ListNode:
        # 使用快慢指针找到链表的中间节点
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 合并两个有序链表
        dummy = ListNode(0)  # 虚拟头节点
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # 将剩余的链表连接到结果中
        if l1:
            current.next = l1
        if l2:
            current.next = l2

        return dummy.next # 真实头节点从虚拟头节点的下一位带实数的节点开始