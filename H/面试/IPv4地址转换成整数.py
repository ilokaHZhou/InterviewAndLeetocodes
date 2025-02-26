# 判断字符串是否为数字
def is_numeric(s):
    return s.isdigit()

# 获取输入的字符串
input_str = input()

# 将输入的字符串按照"#"分割成4个小节
ip_sections = input_str.split("#")

# 如果分割后的小节数量不等于4，则说明输入的IPv4地址格式不正确
if len(ip_sections) != 4:
    print("invalid IP")
else:
    valid = True
    # 遍历每个部分进行检查
    for section in ip_sections:
        if len(section) == 0 or not is_numeric(section):  # 检查是否为空或者是否每部分都是数字
            valid = False
            break
        if len(section) > 1 and section[0] == '0':  # 检查前导零的情况
            valid = False
            break
    
    if not valid:
        print("invalid IP")
    else:
        # 检查第一个小节的范围
        first_section = int(ip_sections[0])  # 将第一个小节转换为整数
        if first_section < 1 or first_section > 128:  # 如果第一个小节的值不在1~128的范围内
            print("invalid IP")
        else:
            # 检查其余3个小节的范围
            for i in range(1, 4):
                section_value = int(ip_sections[i])  # 将当前小节转换为整数
                if section_value < 0 or section_value > 255:  # 如果不在0~255范围内
                    print("invalid IP")
                    break
            else:
                # 计算最终的32位整数
                ip_value = 0
                for i in range(4):
                    ip_value = ip_value * 256 + int(ip_sections[i])  # 每个小节对应一个字节，计算最终的整数值
                print(ip_value)  # 输出最终的32位整数