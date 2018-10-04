from day07.day0701.calculator import Count
#步骤1：导入unittest模块
import unittest
#步骤2：编写测试类TestCount，继承TestCase类
class TestCount(unittest.TestCase):
    #步骤3：重写setUp函数
    def setUp(self):
        print("测试开始")
    #步骤4：编写测试函数test_add1()
    def test_add1(self):
        print("测试两个整数函数")
        c1=Count(10,20)
        res1=c1.add()
        print("计算实际结果：",res1)
    #步骤5：使用unittest提供的断言函数
        self.assertEqual(res1,30)

    #测试两个浮点型数据
    def test_add2(self):
        print("测试两个浮点型数据函数")
        c2=Count(2167.45,3978.78)
        res2=c2.add()
        print("计算实际结果：",res2)
        if abs(res2-6146.23)<0.001:
            res2=6146.23
        self.assertEqual(res2,6146.23)

    #测试两个字符串函数
    def test_add3(self):
        print("测试两个字符串函数")
        c3=Count("你好","测试")
        res3=c3.add()
        print("实际计算结果：",res3)
        self.assertEqual(res3,"你好测试")

    #步骤6：重写tearDown函数
    def tearDown(self):
        print("测试结束")

if __name__=="__main__":
    #步骤7：将测试用例添加到测试套件
    suite=unittest.TestSuite()
    case1=TestCount("test_add1")
    suite.addTest(case1)
    suite.addTest(TestCount("test_add2"))
    case3=TestCount("test_add3")
    suite.addTest(case3)
    #步骤8：执行测试套件
    runner=unittest.TextTestRunner
    runner.run(suite)


