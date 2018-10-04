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