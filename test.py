#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 下午 05:35
# @Email   : pasalai@qq.com
# @Github  : github.com/laishouchao
# @File    : test.py
# @Software: PyCharm

import requests
import time
import random
import json
import DataAnalysis
import visualization


class getInfo(object):
    def __init__(self, page):
        self.url = f"https://m.weibo.cn/comments/hotflow?id=4445005064581909&mid=4445005064581909&max_id={page}&max_id_type=0"
        self.headers = {
            ":authority": " m.weibo.cn", ":method": "GET", ":scheme": "https",
            "accept": "application/json, text/plain, */*", "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "cookie": "cookie: _T_WM=66803180925; XSRF-TOKEN=0df7d1; WEIBOCN_FROM=1110006030; ALF=1578146537; SCF=AhkCB2rNvAv-9nbPzKRrD-HllSeFy8O2oFXjbSOgN5kq_s1vL6Hh8ictmyu7-gzHdSKvs0-LwqyS_zV4n-DHdIc.; SUB=_2A25w7X26DeThGeFO4lYW-SrIyjqIHXVQLgPyrDV6PUNbktAKLVbSkW1NQVRWkkDw6SAqqcB3ZdGSZb0hsax0Ysga; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWypBWbg6zJc73PgN7FFQAe5JpX5KzhUgL.FoM71KBN1KBXeKq2dJLoIp5LxKqL1-BLBKH0q0-0So.0; SUHB=0BL4upNvuRzhCh; SSOLoginState=1575554538; MLOGIN=1; M_WEIBOCN_PARAMS=lfid%3D102803_ctg1_4388_-_ctg1_4388%26luicode%3D20000174%26uicode%3D10000011%26fid%3D102803_ctg1_4388_-_ctg1_4388",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3941.4 Safari/537.36"}

    def Getinfo(self):
        response = requests.get(url=self.url, headers=self.headers).text
        # print(response)
        # with open("test.json", "w", encoding="utf-8") as fp:
        #     fp.write(response)
        return response


if __name__ == '__main__':

    for pageNum in range(1, 301):
        initgetinfo = getInfo(page=pageNum)  # 初始化网络访问
        time.sleep(random.randint(1, 5))
        response = initgetinfo.Getinfo()
        print(response)
        if "data" in response:
            infoJson = json.loads(response)
            infocont = infoJson["data"]["data"]
            with open("AllData.json", "a", encoding="utf-8")as fp:
                fp.write(str(infocont))
        else:
            continue
            # print("[x]Error,Please cheak something ...")
    # 数据分析
    initDataAnalysis = DataAnalysis.dataAnalysis()  # 初始化数据分析接口
    with open("AllData.json", encoding="utf-8") as fp:
        info = fp.read()
    for keywords in range(len(info)):
        keyword = info[keywords]["text"]
        # print(keyword)
        DAresponse = initDataAnalysis.DataAnalysis(keywords=keyword)  # 调用数据分析接口
        print(DAresponse)
    # 数据统计
    list_len = initDataAnalysis.Statistics()
    # 数据可视化
    visualization.visualization(list_len)  # 调用可视化绘图
