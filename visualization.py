#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/11/30 下午 11:39
# @Email   : pasalai@qq.com
# @Github  : github.com/laishouchao
# @File    : visualization.py
# @Software: PyCharm
import time
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Scatter


def pycharts_visit():
    c = (
        Scatter()
            .add_yaxis("负面情绪")
            .add_xaxis("正面情绪")
            .render("散点图.html")
            .set_global_opts(title_opts=opts.TitleOpts(title="Scatter-基本示例"))
    )
    return c


def visualization(list_len):
    bar = Bar()
    bar.set_global_opts(title_opts=opts.TitleOpts(title="热搜情绪分析"))
    bar.set_colors(colors="pink")
    bar.add_xaxis(["<0.1", "<0.2", "<0.3", "<0.4", "<0.5", "<0.6", "<0.7", "<0.8", "<0.9", "<1"])
    bar.add_yaxis("信息数量", list_len)
    bar.render("./outPut/final.html")
    time.sleep(3)  # 给人一种运行起来贼麻烦的仪式感
    print("\n\n[√]可视化页面生成完成！")
