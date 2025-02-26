import os
import re

def extract_filename(html_filename):
    """
    从 HTML 文件名中提取目标部分。
    提取规则：
    1. 提取“(E卷,100分)”或“(E卷,200分)”后第一个短横线后的非空字符串。
    2. 提取到“（Java & Python& JS & C++ & C ）”的第一个左括号之前。
    3. 对提取的字符串进行 strip 处理。
    """
    # 使用正则表达式匹配目标部分
    match = re.search(r"\(E卷,\d+分\)\s*-\s*(.+?)\s*（Java & Python& JS & C\+\+ & C ）", html_filename)
    if match:
        return match.group(1).strip()  # 返回提取的部分并去除空格
    return None

def create_python_file(target_name):
    """
    在当前目录下创建一个新的空 Python 文件。
    如果文件已存在，则跳过。
    """
    python_filename = f"{target_name}.py"
    if os.path.exists(python_filename):
        print(f"文件已存在，跳过: {python_filename}")
        return
    with open(python_filename, "w", encoding="utf-8") as f:
        pass  # 创建一个空文件
    print(f"已创建文件: {python_filename}")

def main():
    # 获取上一级目录中的 E 文件夹路径
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
    e_dir = os.path.join(parent_dir, "H\\", "E")
    print(parent_dir)

    e_dir="D:\Projects\GitHubLocalRepositories\InterviewAndLeetcodes\H\E"

    # 检查 E 文件夹是否存在
    if not os.path.exists(e_dir):
        print(f"错误：文件夹 {e_dir} 不存在！")
        return

    # 遍历 E 文件夹中的所有 HTML 文件
    for filename in os.listdir(e_dir):
        if filename.endswith(".html"):
            # 提取目标部分
            target_name = extract_filename(filename)
            if target_name:
                # 创建新的 Python 文件
                create_python_file(target_name)

if __name__ == "__main__":
    main()