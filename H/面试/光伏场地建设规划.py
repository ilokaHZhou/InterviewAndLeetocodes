def main():
    r, c, s, min_power = map(int, input().split())  # 输入地区长r，宽c，电站边长s，最低发电量min

    # 输入每个区域每平方公里的发电量，存入矩阵matrix中
    matrix = [list(map(int, input().split())) for _ in range(r)]

    # 遍历所有可能的电站位置，计算该位置的矩形区域发电量
    ans = 0
    for i in range(s, r + 1):
        for j in range(s, c + 1):
            square = 0
            for x in range(i - s, i):
                for y in range(j - s, j):
                    square += matrix[x][y]
            if square >= min_power:
                ans += 1

    # 输出结果
    print(ans)


if __name__ == "__main__":
    main()