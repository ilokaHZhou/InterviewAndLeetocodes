class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list()
        for item in s:
            if res and res[-1] == item: # 检查是否要移除栈顶元素
                res.pop()
            else:
                res.append(item)
        return ''.join(res)