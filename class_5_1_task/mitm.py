#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: **
 * @date: 2021/8/10
 * @version: 1.0
 * @fileName: mitm.py
 * @author: 'WangLei'
"""
import json

import yaml
from mitmproxy.tools._main import mitmdump

"""HTTP-specific events."""
import mitmproxy.http


def paramrize_data():
    """
    数据生成器
    :return:
    """
    with open('test_data.yml') as f:
        test_data = yaml.safe_load(f)
    for i, current in enumerate(test_data['mock_data']['current']):
        percent = test_data['mock_data']['percent'][i]
        yield current, percent


class Events:

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        # 数据生成器
        mock_data = paramrize_data()
        # 过滤满足条件的url
        if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
            # 获取响应内容
            resp_json = json.loads(flow.response.content)
            # print(resp_json)
            for i in range(len(resp_json['data']['items'])):
                # 获取数据，取完跳出循环
                try:
                    current, percent = next(mock_data)
                except StopIteration:
                    break
                # 修改响应内容
                resp_json['data']['items'][i]['quote']['name'] = '迪迦奥特曼'+str(i)
                resp_json["data"]["items"][i]["quote"]["current"] = current
                resp_json["data"]["items"][i]["quote"]["percent"] = percent
            # 把修改后的内容赋值给 response 原始数据格式
            flow.response.text = json.dumps(resp_json)



# 实例化请求
addons = [
    Events()
]

if __name__ == '__main__':
    mitmdump(["-s", "mitm.py", "-p", "8080"])
