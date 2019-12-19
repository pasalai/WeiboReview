#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/11/30 下午 10:25
# @Email   : pasalai@qq.com
# @Github  : github.com/laishouchao
# @File    : DataAnalysis.py
# @Software: PyCharm

from snownlp import SnowNLP
import visualization


class dataAnalysis:
    def __init__(self):
        # 初始化数组
        self.temp0 = []
        self.temp1 = []
        self.temp2 = []
        self.temp3 = []
        self.temp4 = []
        self.temp5 = []
        self.temp6 = []
        self.temp7 = []
        self.temp8 = []
        self.temp9 = []

    def DataAnalysis(self, keywords):
        # 情感分析，通过更换微博预料训练生成的.model.3模型可提高分析的精确度
        Affective_value = SnowNLP(keywords)
        # 计算消息的正负面情绪值，并写入Getvalue.xlsx中
        Affective_value_good = Affective_value.sentiments
        Affective_value_bad = 1 - Affective_value_good
        List = [keywords, Affective_value_good, Affective_value_bad]
        print(List[0], List[1], List[2])  # 输出事件及对应的情感值

        # 对情感归类统计
        if Affective_value.sentiments < 0.1:
            self.temp0.append(keywords)
        elif Affective_value_good < 0.2:
            self.temp1.append(keywords)
        elif Affective_value_good < 0.3:
            self.temp2.append(keywords)
        elif Affective_value_good < 0.4:
            self.temp3.append(keywords)
        elif Affective_value_good < 0.5:
            self.temp4.append(keywords)
        elif Affective_value_good < 0.6:
            self.temp5.append(keywords)
        elif Affective_value_good < 0.7:
            self.temp6.append(keywords)
        elif Affective_value_good < 0.8:
            self.temp7.append(keywords)
        elif Affective_value_good < 0.9:
            self.temp8.append(keywords)
        elif Affective_value_good >= 0.9:
            self.temp9.append(keywords)
        else:
            return "err"
        return List

    def Statistics(self):
        # elif endmark == "1":
        #     # final = []
        #     # final.append(temp0)
        #     # final.append(temp1)
        #     # final.append(temp2)
        #     # final.append(temp3)
        #     # final.append(temp4)
        #     # final.append(temp5)
        #     # final.append(temp6)
        #     # final.append(temp7)
        #     # final.append(temp8)
        #     # final.append(temp9)
        #     # # print(final)
        #     # list_len = [len(final[0]), len(final[1]), len(final[2]), len(final[3]), len(final[4]), len(final[5]),
        #     #             len(final[6]),
        #     #             len(final[7]), len(final[8]), len(final[9])]
        list_len = [len(self.temp0), len(self.temp1), len(self.temp2), len(self.temp3), len(self.temp4),
                    len(self.temp5),
                    len(self.temp6), len(self.temp7), len(self.temp8), len(self.temp9)]
        # print(list_len)
        return list_len
