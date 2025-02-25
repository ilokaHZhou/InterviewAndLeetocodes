"""
# 定义运算符优先级
def precedence(operator):
    if operator in ('+', '-'):
        return 1
    if operator in ('*', '/'):
        return 2
    return 0

# 执行具体的运算操作
def apply_operator(operators, values):
    operator = operators.pop()
    right_operand = values.pop()
    left_operand = values.pop()
    if operator == '+':
        values.append(left_operand + right_operand)
    elif operator == '-':
        values.append(left_operand - right_operand)
    elif operator == '*':
        values.append(left_operand * right_operand)
    elif operator == '/':
        values.append(left_operand / right_operand)

# 计算表达式的值
def evaluate(expression):
    values = []  # 用于存储操作数
    operators = []  # 用于存储运算符
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            # 处理多位数字
            num_str = ""
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num_str += expression[i]
                i += 1
            values.append(float(num_str))
            i -= 1
        elif expression[i] == '(':
            operators.append(expression[i])
        elif expression[i] == ')':
            # 遇到右括号，不断进行运算直到遇到左括号
            while operators and operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()  # 弹出左括号
        elif expression[i] in ('+', '-', '*', '/'):
            # 根据运算符优先级进行运算
            while (operators and precedence(operators[-1]) >= precedence(expression[i])):
                apply_operator(operators, values)
            operators.append(expression[i])
        i += 1
    # 处理剩余的运算符
    while operators:
        apply_operator(operators, values)
    return values[-1]

"""
# 以上都不需要

# 读取输入的表达式
expression = input()
# 去除表达式中的多余空格
expression = expression.replace(" ", "")
# 将方括号和花括号替换为圆括号
expression = expression.replace('[', '(').replace(']', ')').replace('{', '(').replace('}', ')')
# 计算并输出结果
# print(int(evaluate(expression)))
print(int(eval(expression)))