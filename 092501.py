# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

sum = 0
n = int (input("請輸入正整數:"))
for i in range (1,n+1):
    sum +=i
print("1 到 %d 的整數和為 %d" % (n,sum))