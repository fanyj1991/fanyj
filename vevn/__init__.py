#!/user/bin/env python
# -*- coding:utf-8 -*-

import os

try:
    os.mkdir("testt.txt")
    f = open("testt.txt")
    f.write("python真好玩，我还要学")
except:
    print("创建错误")

finally:
    print("你懂吗？","不懂？没事，我也不懂")
print("一脸懵逼")