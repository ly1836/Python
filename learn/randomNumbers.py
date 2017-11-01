import random

# lists = [15, 4, 2, 6, 88]
print("测试随机数")
print(random.uniform(1, 56))

# 字符串格式化输出
print("我叫 %s 今年 %d 岁" % ('小明', 21))

# 两个元素的总和确定了下一个数

a, b = 0, 1
while b < 10:
    print(b, end=',')
    a, b = b, a + b

# var = 1
# while var == 1:
#     str = input("输入:")
#     print(str)
#     if str == "exit":
#         break


# 迭代器
print("\n================")
list = [1, 5, 415, 16, 15]

it = iter(list)
for x in it:
    print(x)

# 不定长参数
print("\n================")


def printinfo(args, *flag):
    print("args:", args)
    for x in flag:
        print(x)
    return


printinfo(1, 12, 123, 123, 21)

print("\n================")
# 全局变量和局部变量
total = 0;


def sum(arg1, arg2):
    total = arg1 + arg2
    print("局部变量:", total)
    return


sum(10, 20)
print("全局变量:", total)

print("\n================")
# global 和 nonlocal关键字

num = 1


def fun():
    global num
    print(num)
    num = 123
    print(num)
    return

fun()
print("----------------")

def fun1():
    num = 10
    def iner():
        nonlocal num
        num = 100
        print(num)
        return
    iner()
    print(num)
    return
fun1()