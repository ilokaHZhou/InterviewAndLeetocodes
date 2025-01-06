# 可以用stack后进先出来做
# 用deque实现stack比用list更加线程安全，且deque基于双向链表而list基于动态数组，频繁插入和删除deque不需要频繁分配和释放内存
# 当然python反转数组用reverse更简便：return " ".join(reversed(s.split()))
# 其他语言没有split的可以用双指针挨个反转单词，按数组方式做
class Solution:
    def reverseWords(self, s: str) -> str:
        wordArray = deque(s.split())
        result = []
        while wordArray:
            result.append(wordArray.pop())
        return " ".join(result)

