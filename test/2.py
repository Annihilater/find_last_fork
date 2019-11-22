#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/11/22 17:03
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : 2.py
import requests

from config import PROXIES


def main():
    url = 'https://api.myip.com'

    response = requests.get(url)
    print('ip: {}'.format(response.text.strip()))

    response = requests.get(url, proxies=PROXIES)
    print('tor ip: {}'.format(response.text.strip()))


if __name__ == '__main__':
    main()
