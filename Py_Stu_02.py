'''学习内容：
分支结构的应用场景 - 条件 / 缩进 / 代码块 / 流程图
if语句 - 简单的if / if-else结构 / if-elif-else结构 / 嵌套的if
循环结构的应用场景 - 条件 / 缩进 / 代码块 / 流程图
while循环 - 基本结构 / break语句 / continue语句
for循环 - 基本结构 / range类型 / 循环中的分支结构 / 嵌套的循环 / 提前结束程序
作业：
1. 水仙花数 / 完美数/Fibonacci数列

周日之前完成分支和循环内容的学习'''
# 1.水仙花数(每位数的三次方相加等于这个数的本身)
#for i in range(100,1000):
#    HD = i//100
#    TEN = i%100//10
#    ONE = i%10
#    if (HD**3 + TEN**3 + ONE ** 3) == i:
#        print("%s是水仙花数"%(i))

# 2.完美数（除了自身之外的约数等于它本身的数）
#num = int(input("请输入数字判断是否是完美数："))
#sum = 0
#for i in range(1,num):
#    if num%i==0:
#        sum +=i
#if num == sum:
#    print("%s是完美数"%(num))
#else:
#    print("%s不是完美数"%(num))

# 3.Fibonacci数列（斐波那契数列以兔子繁衍为例子而引入，又称“兔子数列”）
def Fib(NUM):
    if NUM<=1:
        return NUM
    else:
        return Fib(NUM-1)+Fib(NUM-2)

for i in range(1,20):
    print(Fib(i))






