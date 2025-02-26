# 定义一个类Node，用于表示文件系统中的每个目录
class Node:
    def __init__(self, path, parent):
        self.path = path  # 目录的路径
        self.next = {}  # 存储当前目录下的子目录，键为目录名，值为对应的Node对象
        if parent:
            self.next['..'] = parent  # 如果存在父目录，则在子目录映射中添加一个指向父目录的条目

# 检查目录名是否有效的函数，目录名只能包含小写字母
def is_valid_directory_name(name):
    return name.islower() and name.isalpha()  # 如果目录名全部由小写字母组成，则返回true

# 检查是否可以切换到指定的目录的函数，目录名要么是有效的，要么是".."表示上级目录
def is_valid_change_directory(name):
    return name == '..' or is_valid_directory_name(name)  # 如果是".."或者是有效的目录名，则返回true

root = Node('/', None)  # 创建根目录节点，根目录没有父目录，所以第二个参数为None
current_node = root  # 初始化当前目录为根目录
last_output = ''  # 用于存储最后输出的路径

# 循环读取用户输入的命令
try:
    while True:
        input_command = input().strip()  # 读取一行输入并去除前后空格
        if not input_command:
            break
        parts = input_command.split(' ')  # 将输入的命令按空格分割为命令和参数
        command = parts[0]  # 获取命令部分

        if command == 'mkdir' and len(parts) == 2 and is_valid_directory_name(parts[1]):
            # 处理mkdir命令，用于创建新的子目录
            if parts[1] not in current_node.next:
                current_node.next[parts[1]] = Node(current_node.path + parts[1] + '/', current_node)
        elif command == 'cd' and len(parts) == 2 and is_valid_change_directory(parts[1]):
            # 处理cd命令，用于改变当前目录
            next_node = current_node.next.get(parts[1])
            if next_node:
                current_node = next_node  # 如果目录存在，则将当前目录切换为该目录
        elif command == 'pwd' and len(parts) == 1:
            # 处理pwd命令，用于打印当前目录的路径
            last_output = current_node.path  # 将当前目录的路径保存到last_output变量中
except EOFError:
    pass

print(last_output)  # 打印最后保存的路径