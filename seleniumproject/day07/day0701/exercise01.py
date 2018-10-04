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
    def test_exercise01case01(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("张三")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("abcd")
        driver.find_element_by_id("comments").clear()
        driver.find_element_by_id("comments").send_keys("软件测试")
        driver.find_element_by_id("submit").click()
        print("测试case执行完毕！")
        #步骤5:调用断言函数
        self.assertEqual(driver.title,"unittest案例")

    #步骤6：覆盖tearDown（）函数
    def tearDown(self):
        self.driver.quit()
        print("测试完毕！")

#步骤7：调用unittest中的main（）函数，执行测试
if __name__ == "__main__":
    unittest.main()
