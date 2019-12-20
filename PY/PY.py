#!/user/bin/env python
# -*- coding:utf-8 -*-

# 写入 w 清空写入 a模式为往后面加内容写入 b为二进制写入
f = open("D:\\software\\fyjpy\PY\\test.txt","w",encoding="utf-8")
f.writelines(['hello world\n','哈哈\n'])
f.close()
#读取内容 r
#f = open("test.txt","r",encoding="utf-8")
#a=f.readlines()
#print(a)
#f.close()
# with as读取
#with open("test.txt","r",encoding="utf-8") as f:
#    c=f.read()
 #   print(c)

# 类 相当于一个模板，没有实体
#class ClassA1():
   # a1 = 10
  #  def print_a1(self):
   #     print(self.a1)

# 实例化
#c = ClassA1()
#c.print_a1()

import os

try:
    os.mkdir("testt.txt")
        f = open("testt.txt")
            f.write("python真好玩，我还要学")
except:
    print("创建错误")
print("没事，继续运行")
