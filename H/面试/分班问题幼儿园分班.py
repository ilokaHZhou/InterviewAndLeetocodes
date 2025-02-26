nums = input().split()

# 将第一个元素以'/'分隔成两部分，第一部分表示小朋友的编号，第二部分表示是否与前一位小朋友同班
start = nums[0].split('/')
# 创建一个列表class_A，用于存放同班的小朋友的编号
class_A = [start[0]]
# 创建一个列表class_B，用于存放不同班的小朋友的编号
class_B = []

# 创建一个临时列表temp，用于存放两个班级的小朋友编号列表
temp = [class_A, class_B]   

# 遍历nums列表中的每一个元素
for n in nums[1:]:
    # 将当前元素以'/'分隔成两部分，第一部分表示小朋友的编号，第二部分表示是否与前一位小朋友同班
    id_, f = n.split("/")

    # 如果与前一位小朋友同班，则temp不变
    if f == "Y":
        temp = temp
    else:
        # 如果与前一位小朋友不同班，则将temp列表中的两个班级的小朋友编号列表颠倒顺序
        temp = temp[::-1]

    # 将当前小朋友的编号添加到temp列表的第一个班级的小朋友编号列表中
    temp[0].append(id_)

# 如果class_A列表不为空，则按照编号的大小升序排列，并用空格分隔成字符串输出
if class_A:
    print(" ".join(sorted(class_A, key=lambda x: int(x))))
# 如果class_B列表不为空，则按照编号的大小升序排列，并用空格分隔成字符串输出
if class_B:
    print(" ".join(sorted(class_B, key=lambda x: int(x))))