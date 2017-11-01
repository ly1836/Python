
#Python3 面向对象

class MyClass:
    """一个python类"""
    i = 1234

    def f(self):
        return 'hell python'

    def __init__(self):
        print('调用初始化方法')

#实例化类
def newObj():
    x = MyClass()

    # 访问类的属性和方法
    print("x.i => ", x.i)
    print("x.f() => ", x.f())

#newObj()



#继承


class people:
    #姓名
    name = ''
    age = 0

    #定义私有属性,
    __weight = 0

    #定义构造方法
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self._weight = weight

    def speak(self):
        print("%s 说 ：我 %d 岁了"%(self.name,self.age))


x = people('张三',18,113)
# x.speak()
#测试属性私有
print(x.__weight)


class student(people):
    grade = ''

    def __init__(self,n,a,w,g):
        #调用父类构造方法
        people.__init__(self,n,a,w)
        self.grade = g

    #覆写父类方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))

# x = student('张三',18,113,6)
# x.speak()

#另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))


class smple(speaker,student):
    a = ''
    def __init__(self,n,a,w,g,t):
        speaker.__init__(self,n,t)
        student.__init__(self,n,a,w,g)


# test = smple('张三',19,113,3,'hello python')
# test.speak() #方法名同，默认调用的是在括号中排前地父类的方法















