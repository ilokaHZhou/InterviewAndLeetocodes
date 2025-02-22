def move_coordinates(s):
    # 初始化坐标
    x, y = 0, 0
    
    # 分割指令
    commands = s.split(';')
    
    # 遍历指令
    for cmd in commands:
        if len(cmd) < 2 or cmd[0] not in {'A', 'S', 'W', 'D'}:
            continue  # 忽略无效指令
        
        # 提取方向和步长
        direction = cmd[0]
        try:
            step = int(cmd[1:])
        except ValueError:
            continue  # 忽略无效指令
        
        # 更新坐标
        if direction == 'A':
            x -= step
        elif direction == 'D':
            x += step
        elif direction == 'W':
            y += step
        elif direction == 'S':
            y -= step
    
    # 输出结果
    print(f"{x},{y}")

# 读取输入
s = input().strip()
# 计算并输出坐标
move_coordinates(s)