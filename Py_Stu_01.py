'''学习任务：
1. 变量和类型 - 变量的命名 / 变量的使用 / input函数 / 检查变量类型 / 类型转换
2. 数字和字符串 - 整数 / 浮点数 / 复数 / 字符串 / 字符串基本操作 / 字符编码
2. 运算符 - 数学运算符 / 赋值运算符 / 比较运算符 / 逻辑运算符 / 身份运算符 / 运算符的优先级
作业：
 - 华氏温度转换成摄氏温度
 - 输入圆的半径计算周长和面积
 - 输入年份判断是否是闰年'''

#  1.华氏温度转换成摄氏温度
#def Fahh():
#    Fa = int(input("请输入华氏温度："))
#    DC = round(5/9*(Fa-32),2)
#    print("摄氏温度为：%s"%(DC))
#Fahh()

#  2.输入圆的半径计算周长和面积
#from math import pi
#def PmAr():
#    Rad = int(input("请输入半径："))
#    Ar = round(pi * Rad * Rad,2)
#    Pm = round(2 * pi * Rad,2)
#    print("圆的周长等于：%s，圆的面积等于：%s"%(Pm,Ar))
#PmAr()

#   3.输入年份判断是否是闰年
def LY():
    Year = int(input("请输入年份："))
    if Year % 400 == 0 and Year % 100 == 0:
        print("%s是世纪闰年" % (Year))
    elif Year%4==0 and Year%100!=0:
        print("%s是普通闰年"%(Year))
    else:
        print("%s不是闰年" % (Year))
LY()




