# -*- coding: utf-8 -*-

class Group:
    def __init__(self, class_info):
        # course_remained[语文] = [剩余多少节没有排课, 权重, 课程名称]
        self.classInfo = class_info
        self.course_remained = {}
        # 班级数据
        self.class_data = ''
        # 课程表矩阵
        self.course_table = [[''] * 5 for i in range(8)]

        for k, v in self.classInfo.class_distribute.iteritems():
            self.course_remained[k] = [v[0], v[1], k]

    def print_course_remained(self, index):
        print '班级' + str(index), ': 课程', '剩余数量', '权重', '课程名称'
        for k, v in self.course_remained.iteritems():
            print k, v

    def print_course_table(self):
        for row in self.course_table:
            course_str = ''
            for i in row:
                course_str += (str(i) + ' ')
            print course_str
