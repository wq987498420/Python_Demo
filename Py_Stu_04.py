'''学习内容：
字符串的使用 - 计算长度 / 下标运算 / 切片 / 常用方法
列表基本用法 - 定义列表 / 用下表访问元素 / 下标越界 / 添加元素 / 删除元素 / 修改元素 / 切片 / 循环遍历
列表常用操作 - 连接 / 复制(复制元素和复制数组) / 长度 / 排序 / 倒转 / 查找
生成列表 - 使用range创建数字列表 / 生成表达式 / 生成器
元组的使用 - 定义元组 / 使用元组中的值 / 修改元组变量 / 元组和列表转换
集合基本用法 - 集合和列表的区别 / 创建集合 / 添加元素 / 删除元素 / 清空
集合常用操作 - 交集 / 并集 / 差集 / 对称差 / 子集 / 超集
字典的基本用法 - 字典的特点 / 创建字典 / 添加元素 / 删除元素 / 取值 / 清空
字典常用操作 - keys()方法 / values()方法 / items()方法 / setdefault()方法
提交事时间周日，内容上不多，希望大家这个周末把之前所学的东西都复习复习。下周开始学习面向对象的内容。'''
'''字符串的使用 - 计算长度 / 下标运算 / 切片 / 常用方法'''

'''字符串：
    概念：由多字符组合在一起，用引号引起来
    定义：将字符用引号引起来，赋值给变量，单引号和双引号都可以，使用三对单引号定义的可换行显示'''

'''判断字符是否在字符串中：
str="hello python"
if "y" in str:
    print("包含y")
else:
    print("不包含")'''
'''字符串常用方法：
1.index方法， 语法:字符串.index()
str1 = "hello python"
index1 = str1.index('o')   #默认从第一个开始查找
print(index1)   #字符串索引位置
index2 = str1.index('o',6,11)   #定义个范围查找
print(index2)      #字符串索引位置'''
'''2.find方法， 语法：字符串.find()
str1 = "hello python"
index1 = str1.find('o')   #默认从第一个开始查找
print(index1)  #字符串索引位置
index2 = str1.find('o',6,11)   #定义个范围查找
print(index2)   #字符串索引位置'''
'''3.rfind方法(从右边开始查找，但索引不是从右边开始计算的)，语法：字符串.rfind()
str1 = "123.abc.txt"
index1 = str1.rfind('.')
print(index1)'''
'''4.for,while 遍历字符串
str1 = "hello python"    #for遍历
for i in str1:
    print(i)
str1 = "hello python"  #while遍历
i = 0
num = len(str1)
while i<num:  #len()可计算字符串长度(先定义好字符串长度比条件中进行长度计算效率高)
    print(str1[i])
    i +=1'''
'''5.split字符串分割方法，语法：列表=字符串.split(分隔符)
name_list=[]
name = input("请输入姓名（多个用逗号分隔）：")
print(name)
names = name.split('，')   #分割字符串后返回列表
print(names)
name_list.extend(names)
print(name_list)'''
'''6.join方法，语法：字符串=分隔符.join(列表)  #分隔符可为空
name = input("请输入姓名：")
names = name.split('，')
print(names)
str1 = '-'.join(names)   #分隔符可自定义
print(str1)
print("金庸的名著中主角有%s"%str1)'''
'''7.partition方法，语法：元组=字符串.partition(分隔符) #最后返回三个元素组成的元组
str1 = "123.txt"
tuple1 = str1.partition('.')
print(tuple1)
'''
'''8.字符串切片,语法：字符串[开始索引:结束索引:步长]  #步长不写默认为1
str1 = "hello python"
str2 = str1[0:7:2]
print(str2)
'''
'''9.判断字符串中是否都是数字
num = input("请输入证件号：")  #判断字符串是否都是数字组成
if num.isdecimal():
    print("是纯数字")
'''
'''10.判断字符串是否由字母组成
name = input("请输入您的英文名:")  #判断字符串是否都是字母组成
if name.isalpha():
    print("是字母组成")
'''
'''11.字符串大小写转换   小写转大写语法：字符串.upper()  大写转小写语法：字符串.lower()
str1 = "i love you"
str2 = str1.upper()
print(str2)
str3 = "I LOVE YOU"
str4 = str1.lower()
print(str4)
'''
'''列表：列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。列表中的个数和类型不限。（列表使用中括号）
    '''
'''1.通过索引取列表中的元素，语法：l列表[索引]
name = ["关羽","曹操","刘备"]
print(name[0])
print(name[1])
print(name[-1])
'''
'''2.给列表追加元素，语法：列表.append(值)
name = ["关羽","曹操","刘备"]
name.append("大乔")
print(name)
'''
'''3.删除列表中的元素，语法：列表.remove()
name = ["关羽","曹操","刘备"]
name.remove("曹操")
print(name)
'''
'''4.修改列表中的元素，语法：列表[索引]=新值
name = ["关羽","曹操","刘备"]
name[0]="小乔"
print(name)
'''
'''5.查询列表中元素的个数，语法：len(列表)
name = ["关羽","曹操","刘备"]
num = len(name)
print(num)
'''
'''6.遍历列表
name = ["关羽","曹操","刘备"]
for i in name:
    print(i)
'''
'''7.将元素添加到指定位置，语法：列表.insert(索引,值)
name = ["关羽","曹操","刘备"]
name.insert(1,"大乔")
print(name)
'''
'''8.根据索引删除元素，语法：del 列表[索引]
name = ["关羽","曹操","刘备"]
del name[1]
print(name)
'''
'''9.删除并返回删除的元素，语法：列表.pop(索引)
name = ["关羽","曹操","刘备"]
a = name.pop(1)
print(name)
print(a)'''

'''元组：元组和列表一样，也是计算机内存中的一段连续空间，但是元组的特点就是只能查询不能增删改。（元组使用小括号）'''
'''1.元组创建是将元素写入括号中用逗号隔开即可
tup1 = ('Google','Runoob',1997,2000)
tup2 = (1,2,3,4,5)
tup3 = "a","b","c","d"
type(tup3)
<class 'tuple'>
'''
'''1.元组只包含一个元素时要在元素后面加上逗号，否则会被当做运算符使用
tup1 =(50)
print(type(tup1))   #打印出来为int整型

tup2 = (50,)
print(type(tup2))   #打印出来为tuple元组型
'''
'''2.使用下标索引来访问元组中的值：
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
print("tup1[0]:", tup1[0])
print("tup2[1:3]:", tup2[1:3])'''
'''3.元组是不允许修改的，但我们可以对元组进行连接组合
tup1 = (12, 23, 34)
tup2 = ('abc','xyz')
tup3 = tup1 + tup2
print(tup3)'''
'''4.元组是不允许删除的，但我们可以使用del语句来删除整个元组
tup1 = ('Google', 'Runoob', 1997, 2000)
print(tup1)
del tup1
print("删除后的元组：")
print(tup1)'''
'''5.元组运算符：元组和字符串一样，元组之间可以使用+号和*号进行运算。这意味着他们可以组合和复制，运算后生成一个新的元组
print(len(1,2,3))   #计算元素的个数
print((1,2,3)+(4,5,6))   #将两个元组连接成一个元组
print(('HI!',)*4)    #将元组内的元素进行复制
print(3 in (1,2,3))  #判断元素是否存在元组中
for x in (1,2,3):print(x,)  #迭代
'''
'''6.元素索引截取：我们可以通过元素的下标索引截取到一个或一段元素
L = ('Google','Taobao','Runoob')
print(L[2])
print(L[-2])
print(L[1])'''
'''7.元组的内置函数
print(max(1,2,3))  #取元组中最大的值
print(min(1,2,3))  #取元组中最小的值
tuple(list)        #将列表转换成元组
'''
'''字典是python中另一种可变容器模型，可存储任意类型对象
 字典的每个键值（key=>value）对用冒号(:)分割，每个对之间用逗号分隔，整个字典用花括号包括（{}）
 如： d = {key1:value1,key2:value2}
 字典中键必须是唯一的，但值则不必
 值可以取任何数据类型，但键必须是不可变的，如字符串，数字和元组'''
'''字典的操作：1.增加数据，语法：字典[键] = 值
info = {'name':'小名','age':18, 'height':1.75}
print(info)
info['weight'] = 180
print(info)'''
'''2.删除数据，语法：字典.pop(键)   #.pop()删除可将删除的数据通过变量接收
info = {'name':'小名','age':18, 'height':1.75}
print(info)
a = info.pop("name")
print(info)
print(a)'''
'''3.修改数据，语法：字典[键]=值
info = {'name':'小名','age':18, 'height':1.75}
print(info)
info['age']=20
print(info)'''
'''4.查询数据，语法：字典[键值]
info = {'name':'小名','age':18, 'height':1.75}
print(info['name'])'''
'''5.给字典添加键值对，在没有该键值对的时候添加，有则不做处理,语法：字典.setdefault(键,值)
info = {'name':'小名','age':18, 'height':1.75}
info.setdefault('weight',65)   #字典中不存在该键值对则添加元素
print(info)
info.setdefault('height',190)  #字典中存在改键名则不做处理
print(info)
'''
'''6.删除键值对，语法 del 字典[键]
info = {'name':'小名','age':18, 'height':1.75}
del info['name']
print(info)'''
'''修改键值，语法：字典.update(新字典)
info = {'name':'小名','age':18, 'height':1.75}
info.update({'height':1.90})
print(info)
'''
'''清空字典，语法:字典.clear()
info = {'name':'小名','age':18, 'height':1.75}
info.clear()
print(info)
'''
'''根据键取值，键值不存在返回None，不会报错，语法：字典.get(键)
遍历字典中所有的键，语法1：for key in 字典，语法2：for key in 字典.keys()
遍历字典中所有的值，语法：for balue in 字典.balues()
遍历字典中所有的键值对，语法：for item in 字典.items()'''
'''集合(set)是一个无序的不重复元素序列
可以使用大括号{}或者set()函数创建集合，注意：创建一个空集合必须用set()而不是{}，因为{}是用来创建一个空字典
创建格式：parame={value01,value02...}/set(value)
'''
'''1.去重
list1 = ["关羽","曹操","刘备","关羽"]
set1 = set(list1)
print(set1)'''
'''2.快速判断元素是否在集合内
basket = {'orange', 'banana', 'pear', 'apple'}
a = 'orange' in basket
print(a)'''
'''3.两个集合间运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)  # 集合a中包含而集合b中不包含的元素
print(a | b)  # 集合a或b中包含的所有元素
print(a & b)  # 集合a和b中都包含了的元素
print(a ^ b)  # 不同时包含于a和b的元素
'''
'''添加元素，语法：s.add(x)/s.update(x)
   移除元素，语法：s.remove(x)/s.discard(x)/s.pop()
   计算集合元素数，语法：len(s)
   清空集合，语法：s.clear()
   判断元素是否在集合中，语法：x in s'''
