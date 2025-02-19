# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
两种解法：
1.是把每个遍历过的节点放到哈希表里
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

2.是快慢指针，快指针跑两步慢指针跑一步，在环里总会有快指针套圈追上慢指针的情况
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next

        return True