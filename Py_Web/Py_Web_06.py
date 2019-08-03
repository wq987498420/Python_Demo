'''
2.单元测试框架unittest入门
    1.导入unittest包
    2.测试类继承TestCase类
    3.setUp()测试前的初始化工作；tearDown()测试后的清除工作
    注意：
        1.所有类中方法的入参self，定义方法的变量也要 （self.变量）
        2.定义测试用例，以"test"开头命名的方法，方法的入参为self
        3.unittest.main()方法会搜索该模块下所有以test开头的测试用力方法，并自动执行它们
        4.自己写的py文件不能用，用unittest.py命名，不然会找不到TestCase
        执行用例 成功输出.  失败输出F
'''

#import unittest
#
#class UserTestCase(unittest.TestCase):
#    def tearDown(self):
#        print("--tearDown--")
#
#    def setUp(self):
#        print("--setUp--")
#        self.name = "小D课堂"
#        self.age = 28
#
#    def test_name(self):
#        print("调用test_name")
#        #断言是否相同
#        self.assertEqual(self.name, "小D课堂",msg="名字不对")
#
#    def test_isupper(self):
#        print("调用test_isupper")
#        #断言是否为true,msg是断言错误的提示信息
#         self.assertTrue("xdclass".isupper(),msg="不是大写")
#
#    def test_age(self):
#        print("调用test_age")
#        self.assertEqual(self.age,28)
#
#if __name__ == '__main__':
#    UserTestCase()


'''
3.测试套件TestSuite介绍
    需求：
        1.利用unnitest执行流程测试而非单元测试
        2.控制unnitest的执行顺序
    1.unittest.TestSuite() 类来表示一个测试用例集
        1.用来确定测试用例的顺序，哪个先执行哪个后执行
        2.如果一个class中有四个test开头的方法，则加载到suite中是则有四个测试用例
        3.由TestLoder加载TestCase到TestSuite
        4.verbosity参数可以控制执行结果的输出，0 是简单报告、1 是一般报告、 2 是详细报告
            默认1 会在每个成功的用例前面有个“.”每个失败的用例前面有个“F”
    2.TextTestRunner()  文本测试用例运行器
    3.run() 方法是运行测试套件的测试用例，入参为suite测试套件       
'''

#import unittest
#
#class UserTestCase(unittest.TestCase):
#    def setUp(self):
#        print("--setUp--")
#        self.name = "小D课堂"
#        self.age = 28
#
#    def tearDown(self):
#        print("--tearDown--")
#        self.assertEqual("foo".upper(),"FOO")
#
#    def test_one(self):
#        print("test_one 二当家小D 来了")
#        #断言是否相同
#        self.assertEqual(self.name, "小D课堂",msg="名字不对")
#
#    def test_two(self):
#        print("test_two 前端 来了")
#        #断言是否为true,msg是断言错误的提示信息
#        self.assertTrue("XD".isupper(),msg="不是大写")
#
#    def test_three(self):
#        print("test_three  后端 来了")
#        self.assertEqual(self.age,28)
#
#    def test_four(self):
#        print("test_four  小D课堂官网上线啦 https://www.xdclass.net")
#        self.assertEqual(self.age,28)
#
#if __name__ == '__main__':
#    suite = unittest.TestSuite()
#    suite.addTest(UserTestCase("test_one"))
#    suite.addTest(UserTestCase("test_two"))
#    suite.addTest(UserTestCase("test_three"))
#    suite.addTest(UserTestCase("test_four"))
#    runner = unittest.TextTestRunner(Verbosity=1)
#    runner.run(suite)

'''
4.测试套件TestSuite生成测试报告
    1.HTMLTestRunner介绍
        HTMLTestRunner是python标准库的unittest模块的一个扩展，它可以生成HTML的测试报告，无法通过pip安装。
        首先要下HTMLTestRunner.py文件，将下载的文件放入...\python\Lib目录下（或者同个路径）
        
    注意点：python2和python3，语法不一样，导致HTMLTestRunner再python3不兼容
    解决办法：导入课程资料里面修改好的HTMLTestRunner.py (该版本是网上的小伙伴修改好的)
     
'''
import HTMLTestRunner
import unittest
import time

class XdclassTestCase(unittest.TestCase):
    def setUp(self):
        print("--setUp--")
        self.name = "小D课堂"
        self.age = 28

    def tearDown(self):
        print("--tearDown--")
        self.assertEqual("foo".upper(),"FOO")

    def test_one(self):
        #u+用例描述，更直观的了解用例测试点
        u"test_one说明"
        print("test_one 二当家小D 来了")
        #断言是否相同
        self.assertEqual(self.name, "小D课堂",msg="名字不对")

    def test_two(self):
        print("test_two 前端 来了")
        #断言是否为true,msg是断言错误的提示信息
        self.assertTrue("XD".isupper(),msg="不是大写")

    def test_three(self):
        print("test_three  后端 来了")
        self.assertEqual(self.age,28)

    def test_four(self):
        print("test_four  小D课堂官网上线啦 https://www.xdclass.net")
        self.assertEqual(self.age,28)



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(XdclassTestCase("test_one"))
    suite.addTest(XdclassTestCase("test_two"))
    suite.addTest(XdclassTestCase("test_three"))
    suite.addTest(XdclassTestCase("test_four"))
    #runner = unittest.TextTestRunner(Verbosity=1)
    #runner.run(suite)
    #文件名中加了当前时间，为了每次生成不同的测试报告，防止报告被覆盖
    file_prefix = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(file_prefix)
    #创建测试报告，此时这个文件是空文件
    #wb  以二进制格式打开一个文件，只用于写入，如果文件存在则覆盖，不存在则新建
    fp = open("./"+file_prefix+"_result.html","wb")
    #stream定义一个测试报告写入的文件，title就是标日，description就是描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"小D课堂 测试报告", description=u"测试用例执行情况")
    runner.run(suite)
    fp.close()