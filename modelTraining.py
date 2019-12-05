#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 下午 05:09
# @Email   : pasalai@qq.com
# @Github  : github.com/laishouchao
# @File    : modelTraining.py
# @Software: PyCharm

from snownlp import SnowNLP
# 加载情感分析模块
from snownlp import sentiment

text = "".join()  # 文本
s = SnowNLP(text)

# todo snownlp常用方法
print(s.keywords(10))  # 提取 10个关键词  数字代表提取数量
print('/'.join(s.words))  # 分词
print(s.sentences)  # 断句

# s.sentiments  会对文本进行评分

f1 = open('./pos.txt', 'a+')  # 存放正面
f2 = open('./neg.txt', 'a+')  # 存放负面
if s.sentiments < 0.3:  # 可以自定义范围
    print('这是一个负面评价')
    # 这段文本写入neg文件中
    f2.write(text)
    f2.write('\n')

elif s.sentiments > 0.8:  # 可以自定义范围
    print('这是一个正面评价')
    # 这段文本写入pos文件中
    f1.write(text)
    f1.write('\n')
else:
    print('这是一个中性评价')

# 保存此次的训练模型
sentiment.train('neg.txt', 'pos.txt')
# 生成新的训练模型
sentiment.save('sentiment.marshal')