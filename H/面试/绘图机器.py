n , e = map(int, input().split())


if e == 0: # 如果终点横坐标为0
    print(0) # 输出面积为0
    exit()

offsets = [0] * e # 创建一个长度为终点横坐标的整数数组，用于存储纵坐标偏移量

for _ in range(n):
    cur_x , offset_y = map(int, input().split())
    offsets[cur_x] = offset_y # 将偏移量存储在对应横坐标位置上

dp = [0] * e # 创建一个长度为终点横坐标的整数数组，用于存储每个横坐标位置的纵坐标偏移量之和
dp[0] = offsets[0] # 第一个位置的纵坐标偏移量为指令中的纵坐标偏移量
for i in range(1, e): # 从第二个位置开始遍历
    dp[i] = offsets[i] + dp[i - 1] # 当前位置的纵坐标偏移量为指令中的纵坐标偏移量加上前一个位置的纵坐标偏移量之和

ans = 0 # 初始化面积为0
for num in dp: # 遍历每个横坐标位置的纵坐标偏移量之和
    ans += abs(num) # 将绝对值加到面积中
print(ans) # 输出面积