class App:
    """定义App类，用于存储App的相关信息"""

    def __init__(self, name, priority, start_time, end_time):
        self.name = name  # App名称
        self.priority = priority  # App优先级
        self.start_time = start_time  # App允许使用的起始时间（以分钟为单位）
        self.end_time = end_time  # App允许使用的结束时间（以分钟为单位）

def convert_time(time_str):
    """
    时间转换函数，将时间字符串转换为以分钟为单位的整数
    :param time_str: 时间字符串，格式为"小时:分钟"
    :return: 转换后的分钟数
    """
    hours, minutes = map(int, time_str.split(":"))  # 将时间字符串按照":"分割并转换为整数
    return hours * 60 + minutes  # 将小时和分钟转换为分钟

def main():
    n = int(input())  # 读取App数量
    apps = []  # 创建App列表，用于存储所有App

    for _ in range(n):
        # 循环读取每个App的信息，并创建App对象添加到列表中
        app_name, app_priority, app_start_time, app_end_time = input().split()
        app_priority = int(app_priority)
        app_start_time = convert_time(app_start_time)
        app_end_time = convert_time(app_end_time)
        apps.append(App(app_name, app_priority, app_start_time, app_end_time))

    query_time = convert_time(input())  # 读取查询时间，并转换为分钟
    app_at_time = "NA"  # 初始化查询时间对应的App名称为"NA"

    # 创建已注册App列表
    registered_apps = []
    for app in apps:
        if app.start_time >= app.end_time:
            continue  # 如果起始时间不小于结束时间，则跳过

        # 遍历已注册的App列表，检查时间冲突
        for i in range(len(registered_apps) - 1, -1, -1):
            registered = registered_apps[i]
            # 如果存在时间冲突
            if max(app.start_time, registered.start_time) < min(app.end_time, registered.end_time):
                # 如果当前App的优先级高于已注册App的优先级
                if app.priority > registered.priority:
                    registered_apps.pop(i)  # 注销低优先级的App
                else:
                    continue  # 如果优先级不高，继续检查下一个已注册App

        # 将当前App添加到已注册App列表中
        registered_apps.append(app)

    # 遍历已注册App列表，找到查询时间对应的App
    for app in registered_apps:
        if query_time >= app.start_time and query_time < app.end_time:
            app_at_time = app.name  # 更新查询时间对应的App名称
            break  # 找到后退出循环

    print(app_at_time)  # 输出查询时间对应的App名称

if __name__ == "__main__":
    main()