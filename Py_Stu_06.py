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
#异常原理：利用关键字，抛出一个异常类，或者异常类的对象
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
    raise TeleNumError