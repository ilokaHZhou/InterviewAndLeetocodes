num = int(input())
# 将待编码数字转换成二进制字符串
binaryStr = bin(num)[2:]
result = ''

# 每7位一组进行编码
for end in range(len(binaryStr), 0, -7):
    # 取出当前组需要编码的二进制字符串
    currentBinaryStr = binaryStr[max(end - 7, 0):end]
    # 判断当前字节是否为最后一个字节，设置最高位
    flag = '1' if end - 7 > 0 else '0'
    # 将当前字节转换成十进制数
    decimal = int(flag + currentBinaryStr, 2)
    # 将当前字节的十六进制字符串形式添加到结果中
    hexStr = hex(decimal)[2:].upper()
    # 如果十六进制字符串长度为1，需要在前面补0
    hexStr = '0' + hexStr if len(hexStr) == 1 else hexStr
    # 将当前字节的十六进制字符串形式添加到结果中
    result += hexStr

# 返回编码结果的十六进制字符串形式
print(result)