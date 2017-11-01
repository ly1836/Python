"""
运算符练习
"""
a = 21
b = 10
c = 32

c = a + b
print("1 - c 的值为：", c)

c= a % b
print("1 - c 的值为：", c)


print("========================")
"""
Python逻辑运算符
"""
a = 10
b = 34

if(a and b):
    print("1 - 变量 a 和 b 都为 true")

if(a or b):
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")

if not(a and b):
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")

print("========================")
'''
Python成员运算符
'''

a = 34
b = 39

lists = [10, 35, 38, 39, 34, 52]

if a in lists:
    print("1 - 变量 a 在给定的列表中 list 中")

if b not in lists:
    print("2 - 变量 b 不在给定的列表中 list 中")
else:
    print("2 - 变量 b 在给定的列表中 list 中")



print("========================")
'''
Python身份运算符
'''

a = 29
b = 29

if a is b:
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

if a is not b:
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")


