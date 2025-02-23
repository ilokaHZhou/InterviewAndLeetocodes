
def find_kth_to_tail(head, k):
    if not head or k <= 0:
        return None

    fast = head
    slow = head

    # 快指针先走k步
    for _ in range(k):
        if not fast:
            return None
        fast = fast.next

    # 然后快慢指针一起走
    while fast:
        fast = fast.next
        slow = slow.next

    return slow.val


# 示例链表节点类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 多组测试用例处理
while True:
    try:
        # 输入处理
        n = int(input())
        values = list(map(int, input().split()))
        k = int(input())

        # 构建链表
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next

        # 找到倒数第k个节点并输出
        result = find_kth_to_tail(head, k)
        if result is not None:
            print(result)
    except EOFError:
        break
