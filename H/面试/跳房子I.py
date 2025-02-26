def main():
    # 读取一行输入，将其转换为 int 列表 steps
    steps = list(map(int, input()[1:-1].split(',')))

    # 读取房子总格数 count
    count = int(input())

    # 初始化最小索引和为最大整数值
    min_idx_sum = float('inf')
    # 初始化答案为空字符串
    ans = ""

    # 使用两层循环遍历数组中的所有可能的组合
    for idx1 in range(len(steps)):
        for idx2 in range(idx1 + 1, len(steps)):
            # 获取两个步数
            step1 = steps[idx1]
            step2 = steps[idx2]

            # 如果两个步数之和等于 count
            if step1 + step2 == count:
                # 计算当前组合的索引和
                idx_sum = idx1 + idx2
                # 如果当前组合的索引和小于已找到的最小索引和
                if idx_sum < min_idx_sum:
                    # 更新最小索引和
                    min_idx_sum = idx_sum
                    # 更新答案
                    ans = [step1, step2]
                # 找到满足条件的组合后，跳出内层循环
                break

    # 输出结果
    print(ans)


if __name__ == "__main__":
    main()