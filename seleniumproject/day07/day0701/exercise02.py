from selenium import webdriver
#步骤1：导入unittest模块
import unittest
#步骤2：编写测试类
class TestExercise01case01(unittest.TestCase):
    #步骤3：重写setUp函数
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "file:///E:/selenium/day07/day0701demo/exercise01.html"
        print("开始测试：")

    #步骤4：编写测试函数
    def test_case1(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("张三")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("abcd")
        driver.find_element_by_id("comments").clear()
        driver.find_element_by_id("comments").send_keys("软件测试")
        driver.find_element_by_id("submit").click()
        print("测试case1执行完毕！")
        #步骤5:调用断言函数
        self.assertEqual(driver.title,"unittest案例")

    #编写第二条测试用例
    def test_case2(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("abcdeabcde")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("1234567890")
        driver.find_element_by_id("comments").clear()
        driver.find_element_by_id("submit").click()
        print("测试case2执行完毕！")

    #步骤6：覆盖tearDown（）函数
    def tearDown(self):
        self.driver.quit()
        print("测试完毕！")
if __name__ == "__main__":
    #步骤7：对TestSuite实例化，添加测试用例
    suite=unittest.TestSuite()
    case1=TestExercise01case01("test_case1")
    case2=TestExercise01case01("test_case2")
    suite.addTest(case1)
    suite.addTest(case2)
    #步骤8：执行测试用例套件
    runner=unittest.TextTestRunner()
    runner.run(suite)



