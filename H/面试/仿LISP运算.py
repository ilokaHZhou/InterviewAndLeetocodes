import math
numStack = []   # 数字栈
operaStack = []  # 操作符栈

# 计算表达式(param1 op param2)的值
def calc(param1, param2):
    global numStack, operaStack
    op = operaStack.pop()   # 取出操作符
    if op == "add":    # 如果是加法
        numStack.append(param1 + param2) # 将计算结果压入数字栈
    elif op == "sub":  # 如果是减法
        numStack.append(param1 - param2)
    elif op == "mul":  # 如果是乘法
        numStack.append(param1 * param2)
    else:    # 如果是除法
        if param2 == 0:  # 如果除数为0
            print("error")
            exit(0)
        else:
            res = param1 // param2  # 计算商
            numStack.append(res) # 将计算结果压入数字栈


# 处理输入
exp = input() # 读入表达式

mark = 0   # 标记数字串的起始位置
param1 = 0    # 参数1
param2 = 0    # 参数2

for i in range(len(exp)):
    ch = exp[i] # 取出当前字符
    if ch == "(":   # 如果是左括号
        operaStack.append(exp[i + 1:i + 4])    # 取出操作符并压入操作符栈
        i += 4  # 跳过操作符
        mark = i + 1   # 标记数字串的起始位置
    elif ch == ")":   # 如果是右括号
        if mark < i: # 如果有数字串
            numStack.append(int(exp[mark:i])) # 将数字串转为整数并压入数字栈
            i += 1 # 跳过右括号
            mark = i + 1   # 标记数字串的起始位置
        param2 = numStack.pop()    # 取出数字栈顶元素作为参数2
        param1 = numStack.pop()    # 取出数字栈顶元素作为参数1
        calc(param1, param2)   # 计算表达式的值并将结果压入数字栈
    else:
        if ch == " ":   # 如果是空格
            if mark < i: # 如果有数字串
                numStack.append(int(exp[mark:i])) # 将数字串转为整数并压入数字栈
                mark = i + 1   # 标记数字串的起始位置

while len(operaStack) != 0:    # 如果操作符栈非空
    param2 = numStack.pop()    # 取出数字栈顶元素作为参数2
    param1 = numStack.pop()    # 取出数字栈顶元素作为参数1
    calc(param1, param2)   # 计算表达式的值并将结果压入数字栈

ans = numStack[0]   # 取出数字栈顶元素作为表达式的值
print(ans)