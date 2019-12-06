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
import re
import pandas as pd
import DataAnalysis
import visualization


class getInfo(object):
    def __init__(self, page):
        self.url = f"https://api.weibo.com/2/comments/show.json?access_token=2.00AICJkHKHfXOC0ca80471b00LcIop&id=4440448116340041&count=200&page={page}"
        self.headers = {
            "cookie": "Cookie: SINAGLOBAL=8274801057093.762.1564200851915; _s_tentry=open.sina.com.cn; Apache=9305675615267.682.1575617438860; ULV=1575617438977:12:6:6:9305675615267.682.1575617438860:1575611575965; ALF=1607153459; SSOLoginState=1575617459; SCF=AhkCB2rNvAv-9nbPzKRrD-HllSeFy8O2oFXjbSOgN5kq-H72VltZ36uddbJvDlPMobyQOA-5T7hMvehs4NjXtqA.; SUB=_2A25w7nPkDeThGeFO4lYW-SrIyjqIHXVTmuIsrDV8PUNbmtAfLWfxkW9NQVRWkiFq3lCMatdy4gMpV0WTOCYZ6Uf7; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWypBWbg6zJc73PgN7FFQAe5JpX5KzhUgL.FoM71KBN1KBXeKq2dJLoIp5LxKqL1-BLBKH0q0-0So.0; SUHB=0sqR5-faWK_XgW; wvr=6; UOR=,,graph.qq.com; JSESSIONID=7642D42BFB7933B6D7CBC5524CF8CD92; webim_unReadCount=%7B%22time%22%3A1575617801850%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A2%2C%22msgbox%22%3A0%7D",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3941.4 Safari/537.36"}

    def Getinfo(self):
        response = requests.get(url=self.url, headers=self.headers).text
        print(response)
        # 将数据保存到json文件中，防止被反扒后没有数据
        # with open("./outPut/getinfo.json", "a", encoding="utf-8")as fp:
        #     fp.write(response)

        return response


class run:
    def __init__(self):
        self.initList = []

    def run(self):
        for pageNum in range(1, 2):
            initgetinfo = getInfo(page=pageNum)  # 初始化网络访问
            response = initgetinfo.Getinfo()
            if "text" in response:
                infoJson = json.loads(response)
                print(infoJson["comments"][0]["text"])
                for num in range(len(infoJson["comments"])):
                    infocont = infoJson["comments"][num]["text"]
                    # 把一些链接去掉，保留纯文本内容。
                    label_filter = re.compile(r'<span class="url-icon">.*?</span>', re.S)
                    comment = re.sub(label_filter, '', infocont)
                    print(comment)
                    self.initList.append(comment)
                    data = pd.DataFrame(data=self.initList, columns=["评论内容"])
                    data.to_csv("./outPut/评论.csv", mode="a", encoding="utf_8_sig")
            else:
                continue
            return self.initList
        time.sleep(random.randint(1, 5))


if __name__ == '__main__':
    # 数据分析
    initRun = run()
    infoli = initRun.run()
    print(infoli)
    # initDataAnalysis = DataAnalysis.dataAnalysis()  # 初始化数据分析接口
    # with open("AllData.json", encoding="utf-8") as fp:
    #     info = fp.read()
    # print(info)
    # infoList = [info]
    # print(len(infoList))
    # print(info)
    # for keywords in range(len(info)):
    #     print(info[keywords])
    #     keyword = info[keywords]
    #     DAresponse = initDataAnalysis.DataAnalysis(keywords=keyword)  # 调用数据分析接口
    #     print(DAresponse)
    # # 数据统计
    # list_len = initDataAnalysis.Statistics()
    # # 数据可视化
    # visualization.visualization(list_len)  # 调用可视化绘图
