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
        select_id = input("请输入您的选择：")
        return select_id

    # 判断菜单选择是否正确
    def decide_menu(self,sid):
        list1 = list(range(0, 12))
        for i in list1:
            if sid == str(i):
                print("您选择的是:", sid)
                break
        else:
            print("输入错误!")

    def select_function(self,sid,t):
        nofun = ("2", "3", "4", "6", "7", "8", "9", "10", "11", "0")
        self.t = t
        if sid == "1":
            self.t.input_information()
            self.t.output_information()
        elif sid == "5":
            self.t.calculate_salary()
        elif sid in nofun:
            print("功能未实现！")

class TestEngineer():
    # 功能1：输入信息
    def input_information(self):
        self.engineer_information = dict()
        print("-------------------------------")
        print("请输入软件测试工程师的信息:")
        self.engineer_information["engineer_id"] = input("请输入编号:")
        self.engineer_information["engineer_name"] = input("请输入姓名：")
        self.engineer_information["engineer_sex"] = input("请输入性别：")
        self.engineer_information["engineer_work_year"] = int(input("请输入工龄："))
        self.engineer_information["engineer_base_salary"] = float(input("请输入基本工资："))
        self.engineer_information["engineer_performance"] = float(input("请输入绩效："))
        self.engineer_information["engineer_workday"] = float(input("请输入月有效工作天数："))
        self.engineer_information["engineer_InsuranceFee"] = float(input("请输入月保险费："))

    # 功能1：输出信息
    def output_information(self):
        print("-----------------------------------")
        print("输入的工程师的信息如下：")
        print("编号:", self.engineer_information["engineer_id"])
        print("姓名:", self.engineer_information["engineer_name"])
        print("性别:", self.engineer_information["engineer_sex"])
        print("工龄:", self.engineer_information["engineer_work_year"])
        print("基本工资:", self.engineer_information["engineer_base_salary"])
        print("绩效:", self.engineer_information["engineer_performance"])
        print("月有效工作天数:", self.engineer_information["engineer_workday"])
        print("保险费:", self.engineer_information["engineer_InsuranceFee"])
        print("-----------------------------------")

    # 功能5：计算工程师薪资，并输出
    def calculate_salary(self):
        print("计算薪资:")
        self.engineer_information["engineer_foodfee"] = float(input("请输入每日餐补:"))
        self.engineer_information["engineer_befitmonth"] = float(input("请输入月效益："))
        self.engineer_information["TotalSalary"] = (self.engineer_information["engineer_base_salary"] + self.engineer_information["engineer_performance"] +self.engineer_information["engineer_foodfee"] * self.engineer_information["engineer_workday"] +self.engineer_information["engineer_befitmonth"] * self.engineer_information["engineer_work_year"] / 100) * 0.9 - self.engineer_information["engineer_InsuranceFee"]
        print("计算结果：")
        print("---------------------------------------------------------------")
        print("编号:%s\t|姓名:%s\t|本月薪资:%.2f" % (self.engineer_information["engineer_id"], self.engineer_information["engineer_name"],self.engineer_information["TotalSalary"]))
        print("---------------------------------------------------------------")

if __name__=="__main__":
    answer = "y"
    m = Menu()
    t=TestEngineer()
    while answer == "y" or answer == "Y":
        sid=m.menu()
        m.decide_menu(sid)
        m.select_function(sid,t)
        answer = input("是否继续(y/n)?")
    else:
        print("程序结束!")
