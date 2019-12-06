#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 下午 05:09
# @Email   : pasalai@qq.com
# @Github  : github.com/laishouchao
# @File    : modelTraining.py
# @Software: PyCharm

import re
from snownlp import sentiment
import numpy as np
import pymysql
from snownlp import SnowNLP
import matplotlib.pyplot as plt
from snownlp import sentiment
from snownlp.sentiment import Sentiment

conn = pymysql.connect(host='localhost', user='root', password='root', charset="utf8", use_unicode=False)  # 连接服务器
with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM test.weibo WHERE weiboId < '%d'" % 6000000)
    rows = cur.fetchall()
comment = []
for row in rows:
    row = list(row)
    comment.append(row[18])


def train_model(texts):
    for li in texts:
        comm = li.decode('utf-8')
        text = re.sub(r'(?:回复)?(?://)?@[\w\u2E80-\u9FFF]+:?|\[\w+\]', ',', comm)
        socre = SnowNLP(text)
        if socre.sentiments > 0.8:
            with open('pos.txt', mode='a', encoding='utf-8') as g:
                g.writelines(comm + "\n")
        elif socre.sentiments < 0.3:
            with open('neg.txt', mode='a', encoding='utf-8') as f:
                f.writelines(comm + "\n")
        else:
            pass


train_model(comment)
sentiment.train('neg.txt', 'pos.txt')
sentiment.save('sentiment.marshal')
