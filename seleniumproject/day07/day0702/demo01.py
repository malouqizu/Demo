from selenium import webdriver
from selenium.webdriver.common.by import By
#步骤1：导入unittest模块
import unittest
#步骤2：编写测试类
class TestMyCase(unittest.TestCase):
    #步骤3：重写setUp函数
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "file:///E:/selenium/day07/day0702demo/demo01.html"
        print("开始测试：")

    #步骤4、5：编写测试函数,第一条测试用例，测试默认值
    def test_case1(self):
        driver = self.driver
        driver.get(self.base_url)
        print("执行测试用例1，检查默认值是否正确")
        male=driver.find_element(By.XPATH,"//input[@id='male']")
        #判断男选中
        x=male.is_selected()
        self.assertTrue(x)
        #女默认不选中
        female=driver.find_element(By.XPATH,"//input[@id='female']")
        self.assertFalse(female.is_selected())
        #
        weixin=driver.find_element(By.XPATH,"//input[@id='weixin']")
        self.assertTrue(weixin.is_selected())
        #
        music=driver.find_element(By.XPATH,"//input[@id='music']")
        self.assertTrue(music.is_selected())
        print("测试用例1执行完毕")

    #编写第二条测试用例
    def test_case2(self):
        driver = self.driver
        driver.get(self.base_url)
        print("执行测试用例2")
        #点击女
        female = driver.find_element(By.XPATH, "//input[@id='female']")
        female.click()
        self.assertTrue(female.is_selected())
        #
        wangyin=driver.find_element(By.XPATH,"//input[@id='wangyin']")
        wangyin.click()
        self.assertTrue(wangyin.is_selected())
        #
        mounting=driver.find_element(By.XPATH,"//input[@id='mounting']")
        mounting.click()
        self.assertTrue(mounting.is_selected())
        print("测试用例2执行完毕")


    #步骤6：覆盖tearDown（）函数
    def tearDown(self):
        self.driver.quit()
        print("测试完毕！")

if __name__ == "__main__":
    #步骤7：对TestSuite实例化，添加测试用例
    suite=unittest.TestSuite()
    case1=TestMyCase("test_case1")
    case2=TestMyCase("test_case2")
    suite.addTest(case1)
    suite.addTest(case2)
    #步骤8：执行测试用例套件
    runner=unittest.TextTestRunner()
    runner.run(suite)



