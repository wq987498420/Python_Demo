'''什么是面向对象？    面向对象是类比于面向过程的存在
    面向过程：就是按照既定的逻辑顺序，一步一步开发。
    面向对象：把所有逻辑封装成一个一个对象，让对象完成。
    为什么要学习面向对象？   简化开发。
    A：将数据和业务抽象为对象，有利于程序整体结构的分析和设计，使设计思路更加清晰
    B：业务以对象为单位，对象各自完成工作，减少了代码的耦合度，有助于业务升级和代码重构
    C：方便工作划分，有利于提高团队的开发效率

    面向对象的组成：类和对象
        类都是用于创建对象的
    生活中的类和对象：
        类是一类事务的简称
        对象是真实的存在，且具有唯一性
    程序中的类和对象：
        类：专门用于创建对象用的数据类型
        对象：类创建出来的实例
            属性：用于描述对象状态的名词。
            方法：用于描述对象功能的动词。

    类：   class 类():属性+方法
    对象 = 类名()'''

'''类：class 类名(): 属性+方法
class Student():
    def sayHi(self):
        print(
            'I have three things in the world, Moon, sun and you. Moon for night, sun for morning ,and you forever...')

#对象 = 类名()
s1 = Student()
print(s1)
#一个类可以创建多个对象
s2 = Student()
print(s2)
#方法的调用
s1.sayHi()
s2.sayHi()
#属性可以自己添加..对象.属性 = 值
s1.name = "小白"
s1.age = 28
print("%s今年%s岁" % (s1.name, s1.age))
s1.sayHi()
'''
'''#self:代指的就是实例对象本身，那次调用，谁调用就指谁
#自定义类
class Student():
    def say_hi(self):
        print("self:", self, id(self))
        print("大家好，我是一名学生...")
#self的指向问题
s1 = Student()
print("s1:", s1, id(s1))
s1.say_hi()
#另一个对象调用
s2 = Student()
print("s2:",s2, id(s2))
s2.say_hi()'''
'''#在类内部定义属性
#定义类
class Student():
    #python解释器为我们提供了一些方法：魔法方法：满足条件自动调用，不用手动函数名()这样调用。
    #__init__():对象创建完毕以后，立刻调用。（初始化对象...）
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sayHi(self):
        print("%s今年%s岁" % (s1.name, s1.age))
    # def set_attribute(self, name, age):
    # 谁调用这个方法，name/age就绑定到他上面
    # s1.name = name #还有很多对象，不能写死了...
    # self.name = name #self可以代指任何对象，谁调用，self就代指谁。
    # self.age = age self可以代指任何对象，谁调用，self就代指谁。
s1 = Student("小白", 28) #传到类里面的参数，最终会传递给__init__();
s1.sayHi()
'''
'''#__str__(): 这个方法是魔法方法，满足触动条件，自动调用。
   #     触动条件：打印对象的时候，会自动触动__str__();
   #     必须有返回值，且是字符串。
class Student():
    def __init__(self,a, b, c):
        self.name = a
        self.age = b
        self.address = c
    
    def say_hi(self, str1):
        print(self.name, str1)
        
    # 定义__str__()：必须有返回值/
    def __str__(self):
        return "我叫%s,今年%d岁，家住%s"%(self.name,self.age,self.address)
        
s1 = Student("张三",18,"上海")
s1.say_hi("大家好...")
print(s1)'''

'''案例一：烤地瓜
    规则：1.地瓜有自己的状态，默认是生的，地瓜可以进行烧烤
        2.地瓜有自己烧烤总时间，由每次烧烤的时间累加得出
        3.地瓜烧烤时，需要提供本次烧烤的时间
        4.地瓜烧烤时，地瓜状态随着烧烤总时间的变化而变化：0-3生的；3-6半生不熟；6-8熟了；>=8烤糊了
        5.输出地瓜信息时，可以显示地瓜的状态和烧烤的总时间'''
'''
class SweetPotato():
    def __init__(self):
        self.state = "生的"
        self.cook_time = 0
        
    def cooking(self, time):
        #烤地瓜的时间累加得出
        self.cook_time += time
        #地瓜状态随着烧烤总时间的变化而变化
        if 0 <= self.cook_time<3:
            self.state = "生的"
        elif 3<= self.cook_time <6:
            self.state = "半生不熟"
        elif 6= self.cook_time <8:
            self.state = "熟了"
        elif self.cook_time 》=8:
            self.state = "糊了"
            
    def __str__(self):
        return "状态:%s，烧烤总时间为:%d"%(self.state, self.cook_time)
        
s1  = SweetPotato()
s1.cooking(2)
print(s1)'''
'''什么时继承：
    生活中：父亲的财富/能力/智力/颜值，儿子如果直接拥有，就算继承
    程序中：一个类拥有很强大、很好用的功能，另一个类想要拥有可以继承过来
    为什么要继承：简化代码，简化操作。
    什么时候使用继承：
        我们发现一个类，里面的属性和方法太好用，太符合开发逻辑
        我们就不再定义一次了，直接继承就可以了'''
'''体验继承：假设有一个动物类，里面有属性和方法，我们需要自己定义一个狗狗类
            也要这俄格动物类里面的属性和方法，那么就可以继承
#定义一个动物类，里面有属性和方法，将来让别人继承。
class Animal():
    def __init__(self, type1):
        self.type = type1
    def eat(self):
        print(self.type,"需要吃东西")
#体验继承，语法： class 类名（被继承类）:
class Dog(Animal):
    pass
    
d1 = Dog("狗狗")
d1.eat()        
'''
'''继承的语法：class子类（父类）：
        子类：自己觉得别人的属性和方法好，我就要继承别人。（主动继承别人）
        父类：别人觉得我的属性和方法号，主动继承我（被动被继承）（基类/超类）
    根据继承的划分：
        单继承：指子类继承一个父亲
        多层继承：一层一层继承下去，继承几个不重要，重要的是一只继承下去...
        多继承：一个子类继承多个父类。(>=2)'''
'''单继承：class Animal: #类也可以这样定义   默认继承了object
class Animal(object):
    def __init__(self):
        self.type = "哺乳动物"
    def eat(self):
        print(self.type,"需要吃东西...")
        
class Dog(Animal):
    def drink(self):
        print(self.type,"需要喝水...")
        
d1 = Dog()
d1.eat()
d1.drink()'''
'''多层继承：一层一层继承下去，继承几个不重要，重要的是一直继承下去...
        动物->狗->泰迪...'''
'''定义动物类
class Animal(object):
    def __init__(self, type1):
        self.type = type1
    
class Dog(Animal):
    #在原有的基础上，还可以再次增加方法。(增加属性很难)
    def eat(self):
        print(self.type,"需要吃东西...")
    
class Poodle(Dog):
    #在Dog基础上增加属性和方法。
    def drink(self):
        print(self.type,"需要喝水...")
        
p1 = Poodle("泰迪")
p1.eat()
p1.drink()'''

'''#重写： 有的时候我们觉得父类好用，所以继承他，但是他里面的某个方法不好用，我们自己定义吗，那么就需要重写
class Dog(object):
    def __init__(self,type1):
        self.type = type1

    def eat(self):
        print(self.type,"需要吃东西...")

    def drink(self):
        print(self.type,"需要喝水...")

    def bark(self):
     #   其他的属性/方法我们照常继承，但是有一个方法：bark()：泰迪可以可爱点
     #       如果父类中的方法，在子类中不合适，可以重写掉
     #           重写：父类有某个方法，子类中同时定义同名方法，这样子类会使用自己的。类似于叠加掉
        print(self.type, "狂吠不止...")

class Poodle(Dog):
    def bark(self):
        print(self.type, "汪汪叫...")

p1 = Poodle("泰迪")
p1.eat()
p1.drink()
p1.bark()'''


