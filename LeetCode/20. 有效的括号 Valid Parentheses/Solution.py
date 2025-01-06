class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif not stack or stack[-1] != c:
                # 第三种情况：遍历字符串匹配的过程中，栈已经为空了，没有匹配的字符了，说明右括号没有找到对应的左括号 return false (右括号有多余)
                # 第二种情况：遍历字符串匹配的过程中，发现栈里没有我们要匹配的字符。所以return false (左右括号数量一致但有类型对不上的)
                return False
            else:
                stack.pop()

        # 第一种情况：此时我们已经遍历完了字符串，但是栈不为空，说明有相应的左括号没有右括号来匹配，所以return false，否则就return true (左括号有多余)
        return True if not stack else False