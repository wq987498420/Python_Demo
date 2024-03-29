 '''1.什么是函数???
    函数就是可以重复执行的代码块。(用特定的语法包裹)
 2.为什么要使用函数???
    因为函数可以简化代码，简化操作。
 3.什么时候使用函数 + 怎么使用函数???'''
 # 函数体验1: 函数就是可以重复执行的代码块。
# def fn():
#     print('人到中年不得已，保温杯里加枸杞...')
# # 不是函数里面的内容了，出了函数了。
# print(111)
# # 函数调用: 函数名()
# fn()

'''函数不调用不执行。
   使用关键字def定义函数，后面跟一个空格
   空格后面放函数名，不能是关键字，函数名后面+小括号+冒号
   书写函数内部的逻辑的时候，一定要有四个空格，否则就出了函数了。'''
'''为了提高函数与开发人员的交互性，及函数的功能性和可拓展性，python语言为函数提供了参数！
    参数: 形参和实参。
          形参: 形式上参与运算的数或者变量。(占位置用的)
          实参: 实际上参与运算的数或者变量。(真实运算用的)'''
#求两个数的和！
#def get_sum(a, b):  # a和b就是形参。
#    c = a + b
#    print('和是:', c)
#get_sum(1, 1)  # 11都是实参。
# 形参占位置用的。
# 实参真实运算用的，不能多也不能少。

# 想要使用函数内部的值(不是变量)，需要使用关键字return进行返回。
#def foo():
#    num1 = 111
#    print('我是函数foo')
#    return num1
# print(foo())  # 打印执行函数: 打印函数的返回值。
# 没有return默认返回None
# 函数根据返回值和参数，可以划分为四种：
#   1.无参，无返回值。(更倾向于函数功能本身)
# def f1():
#     print('我是函数逻辑，非常厉害...')
#   2.无参，有返回值。(更倾向于函数的计算结果-->给函数外部使用)
# def f2():
#     print('非常厉害的逻辑运算...')
#     return '计算结果'
#   3.有参，无返回值。(更倾向于函数通过参数的传递，体现更强的功能！)
# def f3(str1):
#     print(str1)
#   4.有参，有返回值。(更倾向于函数通过参数的传递，计算出结果，让函数外部使用！)
# def f4(a, b):
#     c = a + b
#     # print(c)  # 打印只是对结果的一种操作而已。
#     return c  # 返回才是非常强大的功能
'''封装一个函数，逻辑中只要某个值多次调用<有可能发生变化>，就设置为参数。
封装一个函数，如果外部想要使用函数的计算结果，那么必须设置返回值。
          现阶段，必须设置返回值。不知道返回什么就不用谢，默认不写返回None.'''

'''变量根据作用范围不同可以分为: 全局变量和局部变量。
    局部变量：只能在函数内部访问的变量。(在函数内部定义的变量)
          优点: 函数执行的时候变量才会在内存中创建，函数执行完毕变量立刻销毁。(占用内存时间短)
          缺点: 只能局部访问，存在时间短。
          return的原因。(函数内部的值外部无法直接使用 --> 函数内部的值是局部变量)
    全局变量：函数外部的变量就是全局变量。(哪里都能够访问)
          优点: 哪里都能够访问，存在时间长。
          缺点: 文件开始全局变量就有了，直到文件结束或者这个变量被删除，内存中才销毁。(占用内存资源)
          注意点: 全局变量，如果想要在函数内部修改必须使用global声明。
  '''
# 局部变量演示
#def fn():
#    str1 = '我是局部变量'
#    print(str1)
#    return str1
#fn()
# 全局范围没有办法访问局部变量
#print(str1)
# 函数，没有办法使用非本(其他)函数中的局部变量。
#   形参也是局部变量。(不同的函数可以使用相同的形参名字)
# def foo(a, b):
#     print(str1)
# 定义一个全局变量
#str1 = '我是全局变量'
#print(str1)
# 在函数中依然能够访问全局变量
#def fn():
    # 局部范围内修改全局变量必须使用global声明。
    #global str1  # global声明: str1操作的是全局变量，不是局部变量。
    # 不做特殊处理，str1就是局部变量了。(尽量不要定义局部变量名字和全局变量名字一样)
    #str1 = '哈哈哈...'  # 如果全局变量中有一个str1,函数内部中想要修改必须有特殊方法，否则就会出现，局部变量中也有一个变量叫做str1；
    # 获取全局变量
    #print(str1)
# 调用函数
#fn()
#print(str1)



