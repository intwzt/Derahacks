# -*- coding: utf-8 -*-
from classInfo import ClassInfo
from group import Group
import random


class Engine:
    def __init__(self, data):
        self.classInfo = ClassInfo(data)
        self.grade = []
        for i in range(8):
            self.grade.append(Group(self.classInfo))

    def print_basic_info(self):
        self.classInfo.print_detail()

    def print_grade_table(self):
        for i in range(8):
            print '第', i+1, '个班级的课表'
            self.grade[i].print_course_table()

    # 返回当前没有被排的课中权值最大的课
    def find_current_max_weight_course(self, gp, row, col):
        sorted_course = sorted(self.grade[gp].course_remained,
                               key=lambda k: self.grade[gp].course_remained[k][1],
                               reverse=True)
        tmp_course = []
        for i in sorted_course:
            tmp_course.append(self.grade[gp].course_remained[i])

        sorted_course = tmp_course

        for c in sorted_course:
            # 如果当前班该课程还有剩余
            if c[0] > 0:
                current_course = c[2]
                count_course = 0
                # 查询当前已经排过该课的其他课表，已排班级数量必须小于老师数量才可排课
                for i in range(8):
                    if self.grade[i].course_table[row][col] == current_course:
                        count_course += 1
                if count_course < self.classInfo.class_distribute[current_course][2]:
                    return current_course

        print 'Error! No result found when find course!'

    # 返回当前没有被排的课的时间点中权值最大的(如果有多个，随机返回一个)
    def find_current_max_weight_dot(self, gp):
        max_count = 0
        max_num = -1
        course_container = []
        # 返回可用排时间点的最大权值和最大权值数量
        for i in range(8):
            for j in range(5):
                # 当前时间没有课程并且该时间点权值比当前权值大
                if len(self.grade[gp].course_table[i][j]) == 0 and self.classInfo.course_weight_table[i][j] > max_num:
                    max_num = self.classInfo.course_weight_table[i][j]
                    max_count = 1
                    course_container = []
                    course_container.append([i, j])
                elif len(self.grade[gp].course_table[i][j]) == 0 and self.classInfo.course_weight_table[i][j] == max_num:
                    max_count += 1
                    course_container.append([i, j])

        # 获得最大权值中随机的一个
        index = 0
        if len(course_container) > 1:
            index = random.randint(1, len(course_container) - 1)

        return course_container[index][0], course_container[index][1]


    # 开始排课
    def start_engine(self):
        for i in range(40):
            for gp in range(8):
                row, col = self.find_current_max_weight_dot(gp)
                course = self.find_current_max_weight_course(gp, row, col)
                # 给课程表塞入课程
                self.grade[gp].course_table[row][col] = course
                # 将当前班当前课程剩余量减一
                self.grade[gp].course_remained[course][0] -= 1

