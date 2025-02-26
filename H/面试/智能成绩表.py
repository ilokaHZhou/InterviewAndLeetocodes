# 导入必要的库
from collections import defaultdict

# 定义学生类
class Student:
    def __init__(self, name):
        self.name = name  # 学生姓名
        self.total_score = 0  # 学生总分
        self.scores = defaultdict(int)  # 存储学生各科成绩的字典，默认值为0

    # 添加成绩的方法，同时累加到总分
    def add_score(self, subject, score):
        self.scores[subject] = score
        self.total_score += score

    # 获取指定科目的成绩
    def get_score(self, subject):
        return self.scores[subject]

# 主函数
def main():
    # 读取学生人数和科目数量
    n, m = map(int, input().split())
    
    # 读取科目名称
    subjects = input().split()
    students = []

    # 读取每个学生的姓名和成绩
    for _ in range(n):
        tokens = input().split()
        student = Student(tokens[0])
        for j in range(m):
            student.add_score(subjects[j], int(tokens[j + 1]))
        students.append(student)

    # 读取用作排名的科目名称
    rank_subject = input()

    # 对学生列表进行排序
    students.sort(key=lambda s: (-s.get_score(rank_subject) if rank_subject else -s.total_score, s.name))

    # 输出排序后的学生姓名
    for student in students:
        print(student.name, end=' ')

# 调用主函数
if __name__ == "__main__":
    main()