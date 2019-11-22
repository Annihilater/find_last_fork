#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/11/22 12:57
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : 1.py
import time

s = 'Oct 9, 2019'
# s = s.replace(',', '')
print(s)
t = time.strptime(s, '%b %d, %Y')
print(type(t))
print(t)
k = time.strftime('%Y-%m-%d', t)
print(k)
