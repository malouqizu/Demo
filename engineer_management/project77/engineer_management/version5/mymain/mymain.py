#版本5：
'''
 1、使用包管理模块
 2、可以输入多个工程师的信息
 3、把现有的功能按照多人去实现
 4、实现功能6，保存信息到文本文件
 5、实现功能11，从文件导入信息
'''
from engineer_management.version5.menu import menu
from engineer_management.version5.testengineer import testengineer

class Mymain():
    def mymain(self):
        m = menu.Menu()
        t = testengineer.Testengineer()
        answer = 'y'
        while answer == 'y' or answer == 'Y':
            m.menu()
            m.select_menu()
            m.select_function(t)
            answer = input("是否要继续？(y/n)")
        else:
            print("程序结束！")

if __name__=="__main__":
    main=Mymain()
    main.mymain()