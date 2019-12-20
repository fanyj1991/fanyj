#!/user/bin/env python
# -*- coding:utf-8 -*-

class Product():
    size='5寸'
    def __init__(self,color):
        self.color=color
    def open(self):
        print('hello world')
    def send_massage(self):
        print('fuck away')

#phone1=Product('土豪金')
#print(phone1.size)
#print(phone1.color)
#phone1.open()
#phone1.send_massage()