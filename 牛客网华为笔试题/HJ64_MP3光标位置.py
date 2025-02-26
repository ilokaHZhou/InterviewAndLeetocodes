def mp3_cursor(n, commands):
    # 初始化当前光标位置和当前显示的歌曲范围
    current = 1
    window_start = 1
    window_end = min(4, n)  # 窗口最多显示4首歌曲

    for cmd in commands:
        if cmd == "U":  # 向上移动
            if current == 1:  # 特殊翻页
                current = n
                window_end = n
                window_start = max(1, n - 3)
            else:
                current -= 1
                if current < window_start:  # 更新窗口
                    window_start = current
                    window_end = min(window_start + 3, n)
        elif cmd == "D":  # 向下移动
            if current == n:  # 特殊翻页
                current = 1
                window_start = 1
                window_end = min(4, n)
            else:
                current += 1
                if current > window_end:  # 更新窗口
                    window_end = current
                    window_start = max(1, window_end - 3)

    # 输出当前窗口和光标位置
    window = list(range(window_start, window_end + 1))
    print(" ".join(map(str, window)))
    print(current)


# 示例输入
n = int(input().strip())
commands = input().strip()
mp3_cursor(n, commands)
