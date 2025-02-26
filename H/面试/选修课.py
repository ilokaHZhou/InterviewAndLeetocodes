class Student:
    def __init__(self):
        self.studentId = ""  # 学生学号
        self.classId = ""  # 班级编号
        self.score1 = -1  # 第一门选修课成绩
        self.score2 = -1  # 第二门选修课成绩

    def getSumScore(self):  # 计算两门选修课成绩和
        return self.score1 + self.score2


def divide(str, courseId, students):
    for sub in str.split(";"):
        tmp = sub.split(",")
        studentId = tmp[0]  # 学生学号
        classId = studentId[:5]  # 班级编号
        score = int(tmp[1])  # 选修课成绩
        if studentId not in students:
            students[studentId] = Student()  # 如果学生还没有被加入HashMap中，则加入
        stu = students[studentId]
        stu.studentId = studentId
        stu.classId = classId
        if courseId == 1:
            stu.score1 = score  # 将第一门选修课成绩加入学生对象中
        else:
            stu.score2 = score  # 将第二门选修课成绩加入学生对象中


scores1 = input()  # 第一门选修课学生的成绩
scores2 = input()  # 第二门选修课学生的成绩
students = {}  # 存储学生信息的字典
divide(scores1, 1, students)  # 将第一门选修课学生成绩划分到字典中
divide(scores2, 2, students)  # 将第二门选修课学生成绩划分到字典中
selectedStudents = [stu for stu in students.values() if stu.score1 != -1 and stu.score2 != -1]  # 选取同时选修了两门选修课的学生
if len(selectedStudents) == 0:
    print("NULL")  # 如果没有同时选修两门选修课的学生，则输出NULL
else:
    ans = {}  # 存储按班级划分的学生信息的字典
    for stu in selectedStudents:
        if stu.classId not in ans:
            ans[stu.classId] = []  # 如果班级还没有被加入字典中，则加入
        ans[stu.classId].append(stu)  # 将学生加入对应班级的列表中
    for classId in sorted(ans.keys()):
        print(classId)  # 先输出班级编号
        studentsInClass = ans[classId]
        studentsInClass.sort(key=lambda stu: (-stu.getSumScore(), stu.studentId))  # 按照成绩和的降序和学号的升序排序
        studentIds = [stu.studentId for stu in studentsInClass]  # 学生学号列表
        print(";".join(studentIds))  # 输出学生学号