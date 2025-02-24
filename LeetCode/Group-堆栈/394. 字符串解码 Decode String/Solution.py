class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # 使用栈存储字符和数字
        current_str = ""  # 当前字符串
        current_num = 0  # 当前数字

        for char in s:  # 遍历字符串
            if char == '[':  # 遇到 '['，入栈当前字符串和数字
                stack.append((current_str, current_num))
                current_str = ""  # 重置当前字符串
                current_num = 0  # 重置当前数字
            elif char == ']':  # 遇到 ']'，出栈并解码
                last_str, num = stack.pop()  # 弹出栈顶的字符串和数字
                current_str = last_str + current_str * num  # 解码当前字符串
            elif char.isdigit():  # 如果是数字
                current_num = current_num * 10 + int(char)  # 计算完整数字
            else:  # 如果是字母
                current_str += char  # 追加到当前字符串

        return current_str  # 返回解码后的字符串