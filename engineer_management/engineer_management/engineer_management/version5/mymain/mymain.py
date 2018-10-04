#版本5：
'''
 1、使用包管理模块
 2、可以输入多个工程师的信息
 3、把现有的功能按照多人去实现
 4、实现功能6，保存信息到文本文件
 5、实现功能11，从文件导入信息
'''
from engineer_management.version5.menu.menu import Menu
from engineer_management.version5.testengineer.testengineer import TestEngineer
class Mymain:
    def __init__(self):
        answer = "y"
        m = Menu()
        t=TestEngineer()
        while answer == "y" or answer == "Y":
            sid=m.menu()
            m.decide_menu(sid)
            if sid !="0": #如果不选择0
                m.select_function(sid,t)
            else:
                print("程序结束，再见！")
                break
            answer = input("是否继续(y/n)?")
        else:
            print("程序结束!")
Mymain()