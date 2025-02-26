class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = deque()
        self.total = 0  # 用于记录队列中元素的总和

    def next(self, val: int) -> float:
        """
        计算新元素加入后的移动平均值。
        """
        if len(self.queue) == self.size:
            # 如果队列已满，移除最早的元素
            self.total -= self.queue.popleft()
        # 将新元素加入队列
        self.queue.append(val)
        self.total += val
        # 计算平均值
        return self.total / len(self.queue)

