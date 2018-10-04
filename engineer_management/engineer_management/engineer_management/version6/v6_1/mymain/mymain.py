'''
版本6：
1、实现剩余未实现的功能
功能3，查询工程师信息
功能7，工程师信息排序
功能10，输出工程师为数据表
'''
from engineer_management.version6.v6_1.menu.menu import Menu
from engineer_management.version6.v6_1.testengineer.testengineer import TestEngineer
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