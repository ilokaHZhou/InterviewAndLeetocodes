"""
递归解法：
def fun(str1, str2):

    if str1 == '' and str2 == '':
        return True
    elif str1 == '' and str2 != '':
        return False
    elif str1 != '' and str2 == '':
        if str1.replace('*', '') == '':
            return True
        else:
            return False
    else:
        m, n = len(str1), len(str2)
        if str1[m-1] == str2[n-1] or (str1[m-1] == '?' and str2.isalnum()):
            return fun(str1[:m-1], str2[:n-1])
        elif str1[m-1] == '*':
            return fun(str1[:m-1], str2) or fun(str1, str2[:n-1])
        else:
            return False

while True:
    
    try:
        str1, str2 = input().lower(), input().lower()
        if fun(str1, str2):
            print('true')
        else:
            print('false')
        
    except:
        break



dp[i][j] 表示字符串 s 的前 i 个字符和模式 p 的前 j 个字符是否匹配
"""


def is_match(s, p):
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]  # 初始化动态规划表
    dp[0][0] = True  # 空字符串匹配空模式
    for j in range(1, n + 1):  # 初始化第一行
        if p[j - 1] == "*":  # 如果模式是 '*'，可以匹配空字符串
            dp[0][j] = dp[0][j - 1]
    for i in range(1, m + 1):  # 遍历字符串
        for j in range(1, n + 1):  # 遍历模式
            if p[j - 1] == "*":  # 如果模式是 '*'
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]  # 匹配多个字符或空字符
            elif p[j - 1] == "?":  # 如果模式是 '?'
                if s[i - 1].isalnum():  # 只能匹配数字或字母
                    dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1].isalpha():  # 如果模式是字母
                # 匹配自身或对应的大小写字母
                if s[i - 1].lower() == p[j - 1].lower():
                    dp[i][j] = dp[i - 1][j - 1]
            else:  # 其他字符（非字母数字）
                if s[i - 1] == p[j - 1]:  # 必须完全匹配
                    dp[i][j] = dp[i - 1][j - 1]
    return dp[m][n]  # 返回最终结果


# 输入处理
p = input().strip()  # 通配符模式
s = input().strip()  # 待匹配字符串
print("true" if is_match(s, p) else "false")
