import sys

index = int(input()) # 输入命令字索引K
input = input() # 输入命令字符串S
charArray = list(input) # 将命令字符串转换为字符数组
command = "" # 当前正在解析的命令字
commandList = [] # 存储解析后的命令字列表

for i in range(len(charArray)):
    ch = charArray[i]

    if ch == '"' and ch in command: # 如果当前字符为双引号且命令字中已经包含了一个双引号
        command += '"' # 将双引号添加到命令字中
        commandList.append(command) # 将解析完毕的命令字添加到命令字列表中
        command = "" # 重置命令字
    elif '"' not in command and ch == '_': # 如果命令字不包含双引号且当前字符为下划线
        if command: # 如果命令字不为空
            commandList.append(command) # 将解析完毕的命令字添加到命令字列表中
            command = "" # 重置命令字
    elif i == len(charArray) - 1: # 如果已经到达字符串末尾
        command += ch # 将当前字符添加到命令字中
        commandList.append(command) # 将解析完毕的命令字添加到命令字列表中
        command = "" # 重置命令字
    else:
        command += ch # 将当前字符添加到命令字中

if index < 0 or index > len(commandList) - 1: # 如果命令字索引超出范围
    print("ERROR")
else:
    commandList[index] = "******" # 将指定索引的命令字替换为******
    result = []

    for item in commandList:
        result.append("_" + item) # 在命令字之前添加下划线

    result = "".join(result)
    result = result[1:] # 删除第一个下划线
    print(result)
