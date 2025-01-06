class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def printLinkedList(node):
    while node:
        print(node.value, end=' -> ' if node.next else '\n')
        node = node.next

def reverseList(head):
    cur = head
    prev = None
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    return prev

def multiplyTwoNumbers(head1, head2):
    dummy_head = ListNode() # 一定要用虚拟头部节点！！可以简化结果链表的构建
    l1 = reverseList(head1)
    l2 = reverseList(head2)

    def getLength(head):
        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    len1 = getLength(l1)
    len2 = getLength(l2)

    result = [0] * (len1 + len2)
        
    p1 = l1
    p2 = l2

    for i in range(len1):
        for j in range(len2):
            result[i + j] += p1.value * p2.value # 当前位的乘积
            result[i + j + 1] += result[i + j] // 10 # 进位到下一位
            result[i + j ] %= 10 # 求余数保留当前位的数字
            p2 = p2.next
        p2 = l2
        p1 = p1.next

    result = result[::-1] # 由于需要向新链表里逆序添加数字，所以要翻转一下

    def removeLeadingZeros(nums):
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                index = i
                break
        return nums[index:]
    
    result = removeLeadingZeros(result)

    current = dummy_head
    for num in result:
        current.next = ListNode(num)
        current = current.next
    
    return dummy_head.next





node_series1_2 = ListNode(2)
node_series1_1 = ListNode(1, node_series1_2)

printLinkedList(node_series1_1)

print()

node_series2_3 = ListNode(5)
node_series2_2 = ListNode(4, node_series2_3)
node_series2_1 = ListNode(3, node_series2_2)

printLinkedList(node_series2_1)

print()

print(printLinkedList(multiplyTwoNumbers(node_series1_1, node_series2_1)))