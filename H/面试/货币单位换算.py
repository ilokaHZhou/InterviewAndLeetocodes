def exChange(unit):
    # 根据货币单位返回其转换为人民币分的汇率
    if unit == "CNY":
        return 100.0  # 人民币
    elif unit == "JPY":
        return 100.0 / 1825 * 100  # 日元
    elif unit == "HKD":
        return 100.0 / 123 * 100  # 港元
    elif unit == "EUR":
        return 100.0 / 14 * 100  # 欧元
    elif unit == "GBP":
        return 100.0 / 12 * 100  # 英镑
    elif unit == "fen":
        return 1.0  # 人民币分
    elif unit == "cents":
        return 100.0 / 123  # 港元分
    elif unit == "sen":
        return 100.0 / 1825  # 日元分
    elif unit == "eurocents":
        return 100.0 / 14  # 欧元分
    elif unit == "pence":
        return 100.0 / 12  # 英镑分
    else:
        return 0.0  # 无效单位返回0


def main():
    n = int(input())  # 读取记录数
    totalFen = 0.0  # 汇总结果

    # 处理每一条货币记录
    for _ in range(n):
        record = input()  # 读取每一行的记录
        amount = 0  # 用于保存金额
        unit = ""  # 保存单位

        # 遍历当前行，逐个提取金额和单位
        for j, c in enumerate(record):
            if c.isdigit():
                amount = amount * 10 + int(c)  # 构建数字
            else:
                unit += c  # 构建货币单位

            # 当遇到完整的金额+单位时进行换算
            if j == len(record) - 1 or (j + 1 < len(record) and record[j + 1].isdigit() and unit):
                totalFen += amount * exChange(unit)  # 计算并累加到总数
                amount = 0  # 重置金额
                unit = ""  # 清空单位

    # 输出汇总结果，只保留整数部分
    print(int(totalFen))


if __name__ == "__main__":
    main()