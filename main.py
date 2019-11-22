#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/11/22 11:32
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : main.py
import time

import requests
from pyquery import PyQuery as pq

from config import PROXIES


class ForkTime:
    """
    获取仓库的 fork 时间
    github 并没有给出 fork 时间，是以 fork 项目的最后一次提交时间记为 fork 时间
    只有当 fork 的用户没有提交的情况下才成立
    run 方法启动
    """

    def __init__(self, start_url: str) -> None:
        """
        :param start_url:仓库 fork 页面url
        """
        self.num = 0
        self.base_url = 'https://github.com'
        self.start_url = start_url
        self.fork_url = None
        self.fork_time = None
        self.data = []
        self.proxies = PROXIES

    def run(self) -> (str, str):
        """
        启动方法
        """
        r = requests.get(self.start_url, proxies=self.proxies)
        doc = pq(r.text)
        forks = doc.find('.repo')
        for fork in forks.items():
            self.num += 1
            self.fork_url = self.base_url + fork.find('a:last-child').attr('href') + '/commits/master'
            print(f'{self.num}  {self.fork_url}')
            self.get_fork_time()
            if self.fork_time:
                self.data.append([self.fork_time, self.fork_url])
            else:
                continue
        self.sort()

    def sort(self) -> (str, str):
        """
        对 fork 时间排序
        :return:
        """
        data = sorted(self.data, reverse=True, key=self.get_key)
        for i in range(len(data)):
            data[i][0] = time.strftime('%Y-%m-%d', data[i][0])  # 时间转字符串
            print(f'{data[i][0]} {data[i][1]}')

    def get_fork_time(self) -> time:
        """
        获取 fork 时间
        :return:time
        """
        r = requests.get(self.fork_url, proxies=self.proxies)

        if r.status_code == 200:
            doc = pq(r.text)
            s = doc.find('.commits-listing .commit-group-title:first-child').text()[11:]
            self.fork_time = time.strptime(s, '%b %d, %Y')  # 字符串转为时间
        elif r.status_code == 404:
            print('库已被删除')
        else:
            print(f'状态码：{r.status_code}')

    @staticmethod
    def get_key(ele: [str, str]) -> time:
        return ele[0]


if __name__ == '__main__':
    url = 'https://github.com/Annihilater/SliderCracker-1/network/members'
    fork_time = ForkTime(url)
    fork_time.run()
