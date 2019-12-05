#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 下午 05:35
# @Email   : pasalai@qq.com
# @Github  : github.com/laishouchao
# @File    : test.py
# @Software: PyCharm

import requests
import json

url = "https://m.weibo.cn/comments/hotflow?id=4445005064581909&mid=4445005064581909&max_id=14763598964247&max_id_type=0"
headers = {"DNT": "1", "Sec-Fetch-User": "?1", "Upgrade-Insecure-Requests": "1",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3941.4 Safari/537.36"}

response = requests.get(url=url, headers=headers)
responseinfo = response.text
print(responseinfo)

infoJson = json.loads(responseinfo)
print(infoJson)
