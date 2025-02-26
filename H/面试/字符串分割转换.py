k = int(input()) # 输入正整数K
s = input() # 输入字符串S
sArr = s.split("-") # 将S按照“-”分隔成N+1个子串
prefix = sArr[0] # 第一个子串
postfixSb = "" # 除第一个子串外的所有子串
for i in range(1, len(sArr)):
    postfixSb += sArr[i]
postfixChars = list(postfixSb) # 将除第一个子串外的所有子串拼接成字符数组
newSb = ""
for i in range(len(postfixChars)): # 将除第一个子串外的所有子串每K个字符组成新的子串，并用‘-’分隔
    if (i + 1) % k == 0 and i + 1 != len(postfixChars):
        newSb += postfixChars[i] + "-"
    else:
        newSb += postfixChars[i]
newSArr = newSb.split("-") # 将新组成的每一个子串按照“-”分隔
resultSb = ""
for str in newSArr: # 对于新组成的每一个子串，如果它含有的小写字母比大写字母多，则将这个子串的所有大写字母转换为小写字母；反之，如果它含有的大写字母比小写字母多，则将这个子串的所有小写字母转换为大写字母；大小写字母的数量相等时，不做转换
    upperCase = sum(1 for c in str if c.isupper())
    lowerCase = sum(1 for c in str if c.islower())
    if upperCase > lowerCase:
        resultSb += str.upper() + "-"
    elif lowerCase > upperCase:
        resultSb += str.lower() + "-"
    else:
        resultSb += str + "-"
postfix = resultSb[:-1] # 将处理后的新组成的每一个子串按照“-”拼接成字符串
print(prefix + "-" + postfix) # 输出转换后的字符串