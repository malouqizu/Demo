#v3_3:选择菜单功能放在单独函数中
class Menu():
    def menu(self):
        print("======================================")
        print("||-------软件测试工程师管理系统------||")
        print("--------------------------------------")
        print("|\t1.输入软件测试工程师资料\t\t  |")
        print("|\t2.删除指定测试工程师资料\t\t  |")
        print("|\t3.查询软件测试工程师资料\t\t  |")
        print("|\t4.修改软件测试工程师资料\t\t  |")
        print("|\t5.计算测试工程师的月薪水\t\t  |")
        print("|\t6.保存新添加的工程师资料\t\t  |")
        print("|\t7.对测试工程师信息排序\t\t\t  |")
        print("|\t(1)编号升序\t\t\t\t\t\t  |")
        print("|\t(2)姓名升序\t\t\t\t\t\t  |")
        print("|\t(3)工龄降序\t\t\t\t\t\t  |")
        print("|\t8.输出所有测试工程师信息\t\t  |")
        print("|\t9.清空所有测试工程师数据\t\t  |")
        print("|\t10.输出软件测试工程师数据表\t\t  |")
        print("|\t11.从文件重新导入测试工程师数据\t  |")
        print("|\t0.结束")
        print("======================================")

        self.select_id = input("请输入您的选择：")
        print("您的选择是", self.select_id)

    # 选择
    def select_menu(self):
        list1 = list(range(0, 12))
        for i in list1:
            if self.select_id == str(i):
                # select_function(sid)
                break
        else:
            print("选择错误！")

    def select_function(self,t):
        nofun=['2','3','4','6','7','8','9','10','11','0']
        self.t=t
        if self.select_id == '1':
            self.t.input_enginfro()
            self.t.output_enginfro()
        elif self.select_id == '5':
            if len(t.enginfor) == 0:
                print("请先输入软件测试工程师的资料信息！")
            else:
                self.t.calculate_salary()
        elif self.select_id in nofun:
            print(self.select_id, "功能未实现！")


class Testengineer():
    def input_enginfro(self):
        self.enginfor = dict()
        print("-------------------------------")
        print("请输入软件测试工程师信息:")
        self.enginfor['engineer_id'] = input("编号：")
        self.enginfor['engineer_name'] = input("姓名：")
        self.enginfor['engineer_sex'] = input("性别：")
        self.enginfor['engineer_workyear'] = int(input("工龄："))
        self.enginfor['engineer_basesalary'] = float(input("基本工资："))
        self.enginfor['engineer_performance'] = float(input("绩效："))
        self.enginfor['engineer_workday'] = int(input("月有效天数："))
        self.enginfor['engineer_insurance'] = float(input("月保险金："))

    def output_enginfro(self):
        print("-------------------------------")
        print("输入的工程师信息如下：")
        print("编号：", self.enginfor['engineer_id'])
        print("姓名：", self.enginfor['engineer_name'])
        print("性别：", self.enginfor['engineer_sex'])
        print("工龄：", self.enginfor['engineer_workyear'])
        print("基本工资：", self.enginfor['engineer_basesalary'])
        print("绩效：", self.enginfor['engineer_performance'])
        print("月有效天数：", self.enginfor['engineer_workday'])
        print("月保险金：", self.enginfor['engineer_insurance'])
        print("-------------------------------")

    # 功能5，计算软件测试工程师工资
    # 要求输入餐补、月效益，然后计算薪资，并显示薪资
    # 总薪资＝（基本工资＋月绩效+餐补╳月有效工作日天数＋月效益╳工龄÷100）╳0.9－月保险金
    def calculate_salary(self):
        print("计算软件测试工程师薪资")
        self.enginfor['engineer_foodfee'] = float(input("请输入餐补："))
        self.enginfor['engineer_befitmonth'] = float(input("请输入月效益："))
        self.enginfor['total_salary'] = (self.enginfor['engineer_basesalary'] + self.enginfor['engineer_performance'] +
                                    self.enginfor['engineer_foodfee'] * self.enginfor['engineer_workday'] +
                                    self.enginfor['engineer_befitmonth'] * self.enginfor['engineer_workyear']) * 0.9 - \
                                    self.enginfor['engineer_insurance']
        print("薪资：", self.enginfor['total_salary'])

if __name__=="__main__":
    m=Menu()
    t=Testengineer()
    answer='y'
    while answer=='y' or answer=='Y':
        m.menu()
        m.select_menu()
        m.select_function(t)
        answer = input("是否要继续？(y/n)")
    else:
        print("程序结束！")