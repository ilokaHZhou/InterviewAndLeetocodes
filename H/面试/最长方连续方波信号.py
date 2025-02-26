import re

signal = input() # 输入信号字符串

pattern = re.compile("^(01)+0$") # 定义正则表达式匹配完全连续交替方波信号

maxLength = 0 # 最长完全连续交替方波信号的长度
result = "-1" # 最长完全连续交替方波信号的字符串

sb = "" # 用于存储当前处理的信号
for c in signal:
    if c == '0' and len(sb) > 0 and sb[-1] == '0': # 当前字符是0，且前一个字符也是0，说明一个完整信号结束
        matcher = pattern.match(sb) # 对当前信号进行匹配
        if matcher and len(sb) > maxLength: # 如果匹配到完全连续交替方波信号，并且长度大于之前的最大长度
            maxLength = len(sb) # 更新最大长度
            result = sb # 更新最大长度对应的字符串
        sb = "" # 清空当前信号

    sb += c # 将当前字符加入当前信号

matcher = pattern.match(sb) # 对最后一个信号进行匹配
if matcher and len(sb) > maxLength: # 如果匹配到完全连续交替方波信号，并且长度大于之前的最大长度
    result = sb # 更新最大长度对应的字符串

print(result) # 输出最长的完全连续交替方波信号串
