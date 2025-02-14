# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 由于链表是逆序存取的，所以从链表头部，即个位开始相加,类似的题要注意可以翻转链表以让低位位于链表头部
        # 每次相加，若结果大于9，则产生进位，进位传递到下一位的相加中
        dummy_head = ListNode() # 一定要用虚拟头部节点！！可以简化结果链表的构建
        current = dummy_head    # 当前节点
        carry = 0   # 进位

        # 当l1,l2或者进位都存在时，继续相加
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0 # 如果l1有节点，取l1的值，否则取0
            val2 = l2.val if l2 else 0 # 如果l2有节点，取l2的值，否则取0

            # 计算当前位数的和
            sum_val = val1 + val2 + carry

            # 计算当前位的值和进位
            carry = sum_val // 10
            current.next = ListNode(sum_val % 10)

            # 移动到下一节点
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy_head.next

