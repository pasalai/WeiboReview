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
            "cookie": "Cookie: SINAGLOBAL=8274801057093.762.1564200851915; wvr=6; _s_tentry=www.baidu.com; Apache=6352301425561.806.1575945766559; ULV=1575945766630:13:7:1:6352301425561.806.1575945766559:1575617438977; ALF=1607481877; SSOLoginState=1575945878; SCF=AhkCB2rNvAv-9nbPzKRrD-HllSeFy8O2oFXjbSOgN5kqCRZSH96yV8fPl7TiizuN9zbfTU4_Fnc5HM7iz1cpBJU.; SUB=_2A25w63bGDeThGeFO4lYW-SrIyjqIHXVTge8OrDV8PUNbmtANLWnckW9NQVRWknLtmOSI5VUJquO4t5Xyv9Z4ocet; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWypBWbg6zJc73PgN7FFQAe5JpX5KzhUgL.FoM71KBN1KBXeKq2dJLoIp5LxKqL1-BLBKH0q0-0So.0; SUHB=0QSpCPOkz_IEJf; UOR=,,graph.qq.com; webim_unReadCount=%7B%22time%22%3A1575953836049%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D; JSESSIONID=F4590F83329600BDFB09BCD7A41F3B97",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3941.4 Safari/537.36"}

    def Getinfo(self):
        print(self.url)
        response = requests.get(url=self.url, headers=self.headers).text
        print(response)
        # 将数据保存到json文件中，防止被反扒后没有数据
        with open("./outPut/getinfo.json", "a", encoding="utf-8")as fp:
            fp.write(response)
        return response


class run:
    def __init__(self):
        self.initList = []

    def run(self):
        for pageNum in range(1, 10):
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
                    with open("./outPut/things.txt", "a", encoding="utf-8") as fp:
                        fp.write(comment + "\n")
                    data = pd.DataFrame(data=self.initList, columns=["评论内容"])
                    data.to_csv("./outPut/评论.csv", mode="a", encoding="utf_8_sig")
            else:
                print("continue")
                continue
            time.sleep(random.randint(1, 5))
            # return self.initList


if __name__ == '__main__':
    # 数据分析
    initRun = run()
    infoli = initRun.run()
    print(infoli)

    initDataAnalysis = DataAnalysis.dataAnalysis()  # 初始化数据分析接口
    with open("./outPut/things.txt", "r", encoding="utf-8") as fp:
        for line in fp:
            # print(line)
            DAresponse = initDataAnalysis.DataAnalysis(keywords=line)  # 调用数据分析接口
    # 数据统计
    list_len = initDataAnalysis.Statistics()
    # 数据可视化
    visualization.visualization(list_len)  # 调用可视化绘图
