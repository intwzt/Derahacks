# -*- coding: utf-8 -*-

# 课时数量及权值
# 总课时：40
# 语文：  9   权重：4
# 数学：  13  权重：6
# 英语：  11  权重：5
# 体育：  3   权重：3
# 音乐：  2   权重：2
# 美术：  2   权重：1

# 代号实际课程映射关系
# 语文：  chinese
# 数学：  math
# 英语：  English
# 体育：  sports
# 音乐：  music
# 美术：  art

# 时间权值：
# 时间(第几节，从0开始)  权重
# 1, 2                 4
# 4, 5                 3
# 0, 6                 2
# 3, 7                 1


class ClassInfo:
    def __init__(self, data):
        # class_distribute[语文] = [总共多少节课，该课的权重, 老师的数量]
        self.class_distribute = {}
        self.course_weight_table = [[0] * 5 for i in range(8)]

        self.class_distribute['chinese'] = [int(data['chinese']), 4, int(data['classSum'])]
        self.class_distribute['math'] = [int(data['math']), 6, int(data['classSum'])]
        self.class_distribute['English'] = [int(data['English']), 5, int(data['classSum'])]
        self.class_distribute['sports'] = [int(data['sports']), 3, int(data['classSum'])]
        self.class_distribute['music'] = [int(data['music']), 2, int(data['classSum'])]
        self.class_distribute['art'] = [int(data['art']), 1, int(data['classSum'])]

        self.assgin_weight(0, 2)
        self.assgin_weight(1, 4)
        self.assgin_weight(2, 4)
        self.assgin_weight(3, 1)
        self.assgin_weight(4, 3)
        self.assgin_weight(5, 3)
        self.assgin_weight(6, 2)
        self.assgin_weight(7, 1)

    def assgin_weight(self, row, weight):
        for i in range(5):
            self.course_weight_table[row][i] = weight

    def print_detail(self):
        print '课程分布:'
        print '课程', '[数量, 权值, 老师数量]'
        for k, v in self.class_distribute.iteritems():
            print k, v
        print '时间权值分布:'
        for row in self.course_weight_table:
            print row
