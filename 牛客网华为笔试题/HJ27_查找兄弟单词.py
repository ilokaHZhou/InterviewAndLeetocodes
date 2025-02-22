# 读取输入
input_data = input().strip().split()
n = int(input_data[0])  # 单词的个数
words = input_data[1:n+1]  # 单词列表
x = input_data[n+1]  # 目标单词
k = int(input_data[-1])  # 查找第 k 个兄弟单词

# 定义兄弟单词的条件
def is_brother(word, target):
    # 长度相同且单词本身不同
    if len(word) != len(target) or word == target:
        return False
    # 字母组成相同
    return sorted(word) == sorted(target)

# 查找所有兄弟单词
brothers = [word for word in words if is_brother(word, x)]
brothers_sorted = sorted(brothers)  # 按字典序排序

# 输出结果
print(len(brothers_sorted))
if k <= len(brothers_sorted):
    print(brothers_sorted[k-1]) # 第k个词的索引是k-1