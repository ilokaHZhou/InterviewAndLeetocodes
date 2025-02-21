# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
1. 哈希表解法，把A链条每个node加入哈希表，遍历B链表看有没有node出现过
2. 双指针法
a, b, c = A长度, B长度, 公共长度
指针A先遍历完链表headA，不要停再继续遍历链表headB，当走到node时，共走步数为：
a+(b−c)
指针B先遍历完链表headB，不要停再继续遍历链表headA，当走到node时，共走步数为：
b+(a−c)

两者相等，假如有公共链，此时A node要么停在公共链头，要么没有公共链会停在空node上
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
