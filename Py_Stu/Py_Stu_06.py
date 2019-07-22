'''#1.打开文件：open(),默认以读取的形式打开
f1 = open("123.txt","r",encoding="utf-8")   #encoding修改读取文件的编码集
str1 = f1.read()
print(str1)
f1.close()
#2.文件写入  打开文件时不能以默认的“r”形式打开，要用“w”写入模式打开
f2 = open("123.txt","w",encoding="utf-8")
#写入内容，也是返回值这个对象的功能， f1.write()
f2.write("hello python!!")   #覆盖功能不是write()，而是oprn(,"w")
f2.write("123")
f2.close()    #一个open()对应一个close()，不能读取完毕直接写入或者写入完毕直接读取。
#边写边读时读不到内容的
f3 = open("123.txt", "w+", encoding="utf-8")
f3.write("123")
#因为能够读写文件，而写入内容后没有关闭，立刻读取，那么就读取不到内容了
print(f3.read())
f3.close()

#open(文件,"r")/open(文件,"w")  前者如果文件不存在直接报错，后者如果文件不存在会新建，如果文件已存在会覆盖
#写 write()
#读：read()(读取所有，可指定大小读取)/readline()(读取一行)/readlines()(读取多行)
#移动插入条光标seek()
#1.写write():
#写入输出很简单。  w:创建新文件/覆盖原有内容。   a:追加到最末尾
#2.读：3个方法
#1.read()   最开始插入条光标在开头，全部读取完毕，在最末尾。  继续读就是""
f1 = open("123.txt", "r")
str1 = f1.read()
print(str1)
print(f1.read())  #在读就是空字符串了
f1.close()

#指定大小读取
f1 = open("123.txt", "r")
print(f1.read(1))
print(f1.read(1))
print(f1.read(4))  #每读一次，光标都会移动
f1.close()

# readlines():读取所有行，放入一个列表中
f1 = open("123.txt", "r")
print(f1.readlines())
f1.close()

#移动插入光标seek()
f1 = open("123.txt", "r")
f1.seek(2)
print(f1.read(1))
f1.close()

#,练习1：指定文件做一个备份
    #思路：创建新文件，名字在原有文件基础上增加一个备份。把源文件里面的所有内容写入新文件
#以读取形式打开一个文件
f1 = open("123.txt", "r")
#以写入形式创建一个文件
f2 = open("123-备份.txt","w")
#从f1中读取内容，写入到f2中
str1 = f1.read()
f2.write(str1)
#关闭两个文件
f1.close()
f2.close()

#练习2：输入一个文件名，在这个名字的后面加上备份，产生一个备份文件
    #逻辑和上面一样
file_name= input("请输入想要备份的文件名：")
#新文件要在file_name的基础上创建
index = file_name.rfind(".")
#新文件 = 文件名 + "-备份" + 后缀名
new_file = file_name[0:index] + "-备份" + file_name[index:]
print(new_file)

f1 = open(file_name,"r")
f2 = open(new_file,"w")
#从老文件中读，写入新文件。防止内存溢出每次读取一部分
while  True:
    #一直读取老文件
    str1 = f1.read(1024)
    #判断如果去到空字符串就跳出循环
    if ""== str1:
        break
    #不是空就写入新文件中
    else:
        f2.write(str1)
f1.close()
f2.close()'''
'''#异常或者程序错误可以捕捉！  try:...except:...
#捕捉异常：有些异常不应该直接导致程序崩溃，因为可能时用户级别的异常。。
try:
    file_name = input("请输入文件名：")
    open(file_name,"r")
    print("文件已读取。。。")
except:
    print("文件不存在")

#捕捉异常的完成语句形式
try:
    file_name = input("请输入文件名：")
    open(file_name, "r")
except NameError as e:  #as是保存的意思，把前面的值，保存到后面的变量里面
    print("这是一个NameError：",e)
except IndexError as e:
    print("这是一个IndexError：", e)
#Exception可以捕捉多个异常
except Exception as e:
    print("这个可以捕捉任何异常：",e)
else:
    print("如果上面异常都没执行，才执行我")
finally:
    print("无论有没有异常，都要最终执行finally代码。")
    #f.close() 一般会这么用

#如果try没有捕捉到指定异常，那么这个异常可以继续向外抛出，外部的try依然能够捕捉
#1.try嵌套
try:
    try:
        print(num1)
    except IndexError as e:
        print(e)
except NameError as e:
    print("外部的try捕获到了这个异常：", e)

#2.函数包裹
def fn():
    try:
        list1 = [1,2,3]
        print(list1[5])
    except NameError :
        print("捕获到了一个NameError...")

try:
    fn()
except Exception as e:
    print("捕获到了函数内部的异常", e)'''
'''#异常原理：利用关键字，抛出一个异常类，或者异常类的对象
#print(111)
#raise NameERROR  #异常类本身，没有对异常的描述。（__str__()）
#print(222)
#所有异常，默认继承Exception类
#自定义异常 类
class TeleNumError(Exception):
    def __str__(self):
        return "Sorry, the number you entered is not 11 !"

str1 = input("请输入11位手机号：")
if len(str1) == 11:
    print("恭喜您输入正确!!!", str1)
else:
    #不是11位报错
    raise TeleNumError '''
#csv是以重纯文本形式储存表格数据的文件。该文件有任意数目的记录组成，每条记录被分隔符分割为字段（最常见的分割符是逗号和制表符）
#且每条记录都有相同的字段序列，因此csv相当于一个结构化表的纯文本形式。
#csv文件读取和写入：在文件读写操作中，常用两种读写方式是列表读写和字典读写
#1.文件读取
#csv文件读取主要是使用reader()和Dictreader()方法，二者均接受一个csv文件参数，并返回一个用于文件读取迭代器
#区别：reader()方法获取的是一行行列表数据的迭代器，每行的数据可通过下标来获取
    #DictReader()方法获取的是一行行字典数据的迭代器，每行的数据可通过键来获取
'''import csv
#列表读取
with open("data.csv","r",encoding="utf-8") as fp:
    reader = csv.reader(fp)  #返回读取迭代器
    titles = next(reader)   #提取出文件记录标题
    print(type(titles))   #<class "list">
    print(titles)    #["id","name","city"]
    for x in reader:    #遍历向下迭代
        print(x)     #["1","Mike", "Beijing"]
        id = x[0]
        name = x[1]
        city = x[2]
        print({"id":id, "name":name,"city":city})

#字典读取
with open("data.csv","r",encoding="utf-8") as fp:
    reader = csv.DictReader(fp)
    for x in reader:
        print(type(x))
        print(x)
        id = x["id"]
        name = x["name"]
        city = x["city"]
        print({"id":id, "name": name, "city": city})'''

#文件写入：writer()用于列表数据写书,DictWriter()用于字典数据写入。#二者使用方法比较简单，但需要注意的是由于是写入文件，需要指明文件，需要指明文件的编码方式（特别是需要写入中文字符时）
import csv
#列表写入
#设置记录标题（列表）和记录值（一个嵌套元组集和列表集列表）
headers = ["id","name","province"]
values = [("001","ShenZhen","GuangDong"),
          ("002","WuHan","HuBei"),
          ("003","ChengDu","SiChuan")]
#使用open函数时设置参数encoding以防乱码
with open("citylist.csv","w",encoding="utf-8", newline="") as fp:
    writer = csv.writer(fp)
    writer.writerow(headers)
    writer.writerows(values)

#字典写入
#设置记录标题（列表）和记录值（一个嵌套字典集的列表）
headers = ["id","name","province"]
values = [{"id":"001","name":"ShenZhen","province":"GuangDong"},
        {"id":"002","name":"WuHan","province":"HuBei"},
        {"id":"003","name":"ChengDu","province":"SiChuan"} ]
with open("citydict.csv","w",encoding="utf-8",newline="") as fp:
    writer = csv.DictWriter(fp,headers)
    writer.writeheader()
    writer.writerows(values)

#在打开待写入csv文件时，这里我们还传入了一个newline参数，并且其值为空字符串，这么做是为了防止在每次写完一行后
#其会自动再写入一个换行符，如下文为设置和不设置newline的文件写入对应结果：
#设置了newline的文件写入结果：
'''
id,name,province
001,ShenZhen,GuangDong
002,WuHan,HuBei
003,ChengDu,SiChuan'''
#未设置newline的文件写入结果：
'''
id,name,province

001,ShenZhen,GuangDong

002,WuHan,HuBei

003,ChengDu,SiChuan

'''
#JSON是一种轻量级的数据交换格式，简洁和清晰的层次结构使得JSON成为理想的数据交换语言。易于人阅读和编写，同时也易于机器解析和生成，并有效地提升网络传输效率。
#使用JSON函数，导入JSON库：import JSON
#json.dumps  将python对象编码成JSON字符串
#json.loads  将已编码的JSON字符串解码为python对象
#json.dumps 用于将python对象编码成json字符串。
#语法：json.dumps(obj,skipkeys=False, ensure_ascii = True,check_circular=True,allow_nan=True,
#cls=None,indent=None,separators=None,encoding="utf-8",default=None,sort_keys=False,**kw)
#import json
#data = [{"a":1,"b":2,"c":3,"d":4,"e":5}]
#json = json.dumps(data)
#print(json)
#打开键值排序、缩进为4，以",",":"为分隔
#import json
#data = [{"a":1,"b":2,"c":3,"d":4,"e":5}]
#json = json.dumps(data,sort_keys=True,indent=4,separators=(",",":"))
#print(json)
#json.loads用于解码JSON数据，该函数返回python字段的数据类型。
#语法：json.loads(s,encoding=None,cls=None,object_hook=None,parse_float=None,parse_int=None,
#parse_constant=None,object_pairs_hook=None,**kw)
import json
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
text = json.loads(jsonData)
print(text)

