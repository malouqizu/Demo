from day07.day0702.MyModuleA import MyOne
import unittest
class TestMyOne(unittest.TestCase):
    def setUp(self):
        print("开始测试")

    def test_first_second1(self):
        m1=MyOne()
        r1=m1.first()
        r2=m1.second()
        self.assertIn(r2,r1,"没有找到数据")

    def test_third1(self):
        m2=MyOne()
        m2.third()

    def tearDown(self):
        print("测试结束")

if __name__=="__main__":
    suite=unittest.TestSuite
    case1=TestMyOne("test_first_second1")
    case2=TestMyOne("test_third1")
    suite.addTest(case1)
    suite.addTest(case2)
    runner=unittest.TextTestRunner()
    runner.run(suite)