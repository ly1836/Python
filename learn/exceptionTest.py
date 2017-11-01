
#测试异常捕获处理
while True:
    try:
        num = int(input("please you input:"))
        if num == 123:
            raise ValueError("value ")
    except ValueError:
        print("value type error!")
        break