import unittest

#数据类型
counter = 100 #赋值整型变量
miles = 1000.9 #赋值浮点型
name = "leiyang" #字符串

print(counter),
print(miles)
print(name)

print("==========================")
#变量赋值
name = miles = counter
print(name)

print("==========================")
#判断类型
a = 1
b = 2.3
c = True
d = 4+3j
e = "qwe"
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print(isinstance(a, int))

print("==========================")



class A:
    pass


class B(A):
    pass

print(isinstance(A(),A))
print(isinstance(B(),A))
print(type(B()) == A)
print(type(A()) == A)

print("==========================")
#字符串操作
word = "hello word!"
print(word[2])
print("hello\nword")
print(r"hello\nword")

print("==========================")
#列表操作

list = ['abc','ly','python','dasdv']
tinylist = [123, 'runoob']

print(list)
print(list[0:1])
print(list[0:-1])
print(list[1] * 2)
list[1] = 'ly1'
print(list + tinylist)

print("==========================")
#元组

tuple = ('abc','ly','python','dasdv','ly')
print(tuple)
print(tuple[0:1])
print(tuple[0:-1])
print(tuple[1] * 2)

print(type(tuple))


import os
os.system("d:")
os.system('curl -H "Content-Type:text/plain" --data-binary @urls.txt "http://data.zz.baidu.com/urls?site=www.leiyang.group&token=zejntld0YmjA5IyF" ')













