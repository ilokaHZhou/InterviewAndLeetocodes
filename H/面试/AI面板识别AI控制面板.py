import heapq

# 灯对象，包含 id, x 坐标, y 坐标 和 半径 r
class Light:
    def __init__(self, id, x, y, r):
        self.id = id
        self.x = x
        self.y = y
        self.r = r

    # 定义排序规则：按 y 坐标排序
    def __lt__(self, other):
        return self.y < other.y

def main():
    n = int(input())  # 读取灯的数量
    pqY = []  # 按 y 坐标排序的优先队列（最小堆）

    # 读取灯的数据并添加到优先队列
    for _ in range(n):
        data = list(map(int, input().split()))  # 读取一行并分割为整数列表
        id, x1, y1, x2, y2 = data
        cx = (x1 + x2) // 2  # 中心 x 坐标
        cy = (y1 + y2) // 2  # 中心 y 坐标
        rad = (x2 - x1) // 2  # 半径
        heapq.heappush(pqY, Light(id, cx, cy, rad))  # 将灯对象加入到 y 坐标最小堆

    result = []  # 存储最终输出的灯编号
    pqX = []  # 按 x 坐标排序的最小堆

    # 处理每一行灯
    while pqY:
        ref = heapq.heappop(pqY)  # 弹出当前行的基准灯
        heapq.heappush(pqX, ref)  # 将基准灯添加到当前行

        # 查找并添加同一行的灯
        while pqY and abs(pqY[0].y - ref.y) <= ref.r:
            heapq.heappush(pqX, heapq.heappop(pqY))

        # 按 x 坐标顺序输出同一行的灯编号
        while pqX:
            result.append(str(heapq.heappop(pqX).id))

    print(" ".join(result))  # 输出结果

main()