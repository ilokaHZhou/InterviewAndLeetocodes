# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
1.把值取出来然后翻转对比看是否一致
2.反转链表法

大体上以下几步：
1.找到前半部分链表的尾节点。
2.反转后半部分链表。
3.判断是否回文。
4.恢复链表。
5.返回结果。
"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]