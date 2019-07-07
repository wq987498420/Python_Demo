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
'''列表：列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。列表中的个数和类型不限
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

'''元组'''
