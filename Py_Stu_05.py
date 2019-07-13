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
'''需求：父类中有一个bark()，但是子类额要在这个方法的基础上加强。
    1.重写
    2.在子类中调用父类被重写的方法 
    3.在这基础上添加新代码...'''
'''#父类狗狗类
class Dog(object):
    #定义属性
    def __init__(self,type1):
        self.type = type1
    #定义方法
    def eat(self):
        print(self.type,"需要吃东西...")
    def bark(self):
        print(self.type,"汪汪叫...")

#子类继承父类
class Poodle(Dog):
    #父类的bark方法，功能不全，所以：
    #1.重写
    def bark(self):
        #2.调用父类被重写的方法：
        #a.super().bark()
        super().bark()
        #b.super(子类,self).bark()  #不写有默认值
        super(Poodle, self).bark()
        #c.父类.bark()
        Dog.bark(self)
        #添加新代码
        print(self.type,"摇尾巴...")

p1 = Poodle("泰迪")
p1.bark()'''
'''#需求：Dog类只有type属性，泰迪狗希望在原有基础上添加name/age；
class Dog(object):
    def __init__(self, type1):
        self.type = type1

    def eat(self):
        print(self.type,"需要吃东西...")

#子类继承父类后，添加name/age
class Poodle(Dog):
    #添加name/age，需重写__init__方法
    def __init__(self, name, age, type1):
        #子类重写父类后，父类的__init__()将不会执行那么type属性就不会被绑定了
        #1.手动绑定父类的type属性；2.手动调用父类的__init__()
        #方法一
        super().__init__(type)
        #方法二（几乎不用）
        super(Poodle, self).__init__(type1)
        #方法三
        Dog.__init__(self,type1)
        #添加新属性
        self.name = name
        self.age = age
p1 = Poodle("小灰灰",2,"泰迪")
print(p1.name,p1.age,p1.type)'''
'''需求：假设两个甚至三个类里面的属性和方法都很好用，那么子类能不能继承'''
'''#定义一个神仙类
class God(object):
    #定义不涉及属性
    def fly(self):
        print("飞...")
    #定义方法
    def speak(self):
        print("说人话...")
#定义普通动物类
class Animal(object):
    def run(self):
        print("跑...")
    def speak(self):
        print("说兽语...")
# 定义一个坐骑类：多继承就是一个子类，继承多个父类。
class ZuoJi(God,Animal):
    # 让动物技能说人话有能说兽语的
    def speak(self):
        # 有选择
        str1 = input("1说人话，2说兽语")
        if str1 == "1":
            #说人话，调用God父类的speak方法
            God.speak(self)
        elif str1 == "2":
            #说兽语，调用Animal父类的speak方法
            Animal.speak(self)
        else:
            print("没有此类语言所对应!!!")

z1 = ZuoJi()
z1.run()
z1.fly()
#多继承，如果多个类都有同一方法：默认执行第一个被继承的父类中的方法。（后面的都不执行了）
z1.speak()
#拓展：子类继承了哪些父类？？继承顺序什么样？？
# print(ZouJi.__mro__)   #返回值是一个元组：继承顺序，从自身开始一直到所有父类，包括object'''
'''#私有属性：只能类内部访问，外部无法访问的属性。
#   女孩的年龄，男孩的存款，就业人事的薪资。。。
#定义女孩类
class Girl(object):
    def __init__(self, name, age):
        self.name = name
        # 年龄私有
        self.__age = age
    #定义一个方法，向外部提供有私有私有属性的方法
    def get_age(self):
        return self.__age
    #定义一个方法，修改内部私有属性
    def set_age(self, num):
        self.__age = num

g1 = Girl("小红", 18)
print(g1.name)
#print(g1.__age)   #无法访问

# 修改私有属性和获取私有属性
g1.set_age(28)
print(g1.get_age())
#私有属性可以被继承，但能否被访问，就看类是否提供方法了。
    #注意：晚上答题按照不能继承回答
class New_Girl(Girl):
    pass
g2 = Girl("小白", 28)
#设置和获取私有属性
print(g1.get_age( ))
g1.set_age(88)
print(g1.get_age())
'''
'''
面向对象三大特征：
    1.封装：把功能和属性封装到一个对象中，对外提供方法，隐藏现实。
    2.继承：子类可以使用父类的属性和方法
    3.多态：使用一个对象的地方，同样可以使用他的子类对象。
    # 人吃肉   传肉给人吃   如果汉堡继承了肉   传汉堡也可以

class Meat(object):
    def __init__(self):
        self.type = "肉"
class Ham(Meat):
    #汉堡除了肉还有别的东西
    def __init__(self):
        #调用父类中的__init__()
        super().__init__()
        self.type += "+(面包+蔬菜+萨拉...)"
class Person(object):
    def eat_meat(self,meat):
        print("吃%s"%meat.type)

    def eat_meat(self, ham):
        print("吃%s" % ham.type)
p1 = Person()
m1 = Meat()
h1 = Ham()

p1.eat_meat(m1)
p1.eat_meat(h1)
 '''

