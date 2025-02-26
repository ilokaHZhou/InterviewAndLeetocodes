def egyptian_fraction(numerator, denominator):
    result = []  # 存储埃及分数
    while numerator != 1:  # 当分子不为 1 时循环
        if denominator % numerator == 0:  # 如果分母能被分子整除
            denominator = denominator // numerator  # 更新分母
            numerator = 1
        else:
            unit_denominator = denominator // numerator + 1  # 计算单位分数的分母
            result.append(f"1/{unit_denominator}")  # 添加单位分数
            # 更新分子和分母
            numerator = numerator * unit_denominator - denominator
            denominator = denominator * unit_denominator
    result.append(f"1/{denominator}")  # 添加最后一个单位分数
    return result  # 返回埃及分数列表


# 输入处理
numerator, denominator = map(int, input().split("/"))
result = egyptian_fraction(numerator, denominator)
print("+".join(result))
