from engineer_management.version4.v4_2.menu import Menu
from engineer_management.version4.v4_2.testengineer import TestEngineer
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