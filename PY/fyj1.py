#!/user/bin/env python
# -*- coding:utf-8 -*-
import json
j = '''
{"name":"小明",
"sex":"未知"
}
'''
#json转字典
c = json.loads(j)
c["sex"] = "男"
print(c)
#字典转json
c = json.dumps(j,ensure_ascii=False)
print(j)

# random 获取随机数
import random

a = random.randint(22,25)
print(a)

m = random.choice("sfgm")
print(m)
# 获取文件的绝对路径
import os
p = os.path.abspath("test.txt")
print(p)

# 获取文件夹路径
k = os.path.dirname(p)
print(k)

# 获取文件名
y = os.path.basename(p)
print(y)

# 拼接目录和文件
o = os.path.join(k,y)
print(o)
# 创建文件夹
os.mkdir("fyj2")




