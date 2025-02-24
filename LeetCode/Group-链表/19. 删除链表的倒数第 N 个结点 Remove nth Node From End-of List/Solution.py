# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # 创建虚拟头节点
        fast = slow = dummy  # 快慢指针初始化为虚拟头节点

        # 快指针先移动 n+1 步，因为是从dummy node开始而不是第一个node开始，因此是n+1
        for _ in range(n + 1):
            fast = fast.next

        while fast:  # 快慢指针同时移动，直到快指针到达链表末尾
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next  # 删除倒数第 n 个节点
        return dummy.next  # 返回链表的头节点