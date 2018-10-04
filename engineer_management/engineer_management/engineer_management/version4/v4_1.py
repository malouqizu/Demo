#v4:
'''
版本3已经完成功能：功能1，输入信息，功能5，计算薪资
本版本要求实现：
功能2，删除工程师信息
功能4，修改工程师信息
功能8，输出工程师信息
功能9，清空工程师信息
功能0，结束
'''
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

    #版本4实现2、4、8、9、0功能，对选择进行相应的判断
    def select_function(self,sid,t):
        nofun = ("3","6", "7", "10", "11")
        self.t = t
        if sid == "1":
            self.t.input_information()
            self.t.output_information()
        #版本4实现：删除工程师信息
        elif sid=="2":
            confirm1=input("是否真的删除工程师信息？(Y/N)")
            if confirm1=="y" or confirm1=="Y":
                self.t.del_information()
            else:
                print("您已取消删除。")
        # 版本4实现：修改工程师信息
        elif sid=="4":
            print("1.修改全部信息\n2.修改部分信息")
            select1 = input("请选择：")
            if select1 == "1":
                self.t.update_all_information()
            elif select1 == "2":
                self.t.update_partial_information()
            else:
                print("选择错误!")
        #计算薪资
        elif sid == "5":
            self.t.calculate_salary()
        #版本4实现：输出所有信息
        elif sid=="8":
            self.t.output_all_information()
        #版本4实现：清空所有信息
        elif sid=="9":
            confirm2=input("是否真的清空工程师信息？(Y/N)")
            if confirm2=="y" or confirm2=="Y":
                self.t.clear_information()
            else:
                print(" 取消清空！")
        elif sid in nofun:
            print("功能未实现！")

class TestEngineer():
    #构造函数，初始化数据
    def __init__(self):
        self.engineer_information = dict()
        self.init_data()

    #功能1：输入信息
    def input_information(self):
        #self.engineer_information = dict()
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

    #功能2：删除工程师信息
    def del_information(self):
        #del self.engineer_information
        self.init_data()
        print("数据删除成功！")

    #功能4：修改工程师所有信息
    def update_all_information(self):
        print("-------------------------------")
        print("请修改软件测试工程师的信息:")
        self.engineer_information["engineer_id"] = input("请输入新的编号:")
        self.engineer_information["engineer_name"] = input("请输入新的姓名：")
        self.engineer_information["engineer_sex"] = input("请输入新的性别：")
        self.engineer_information["engineer_work_year"] = int(input("请输入新的工龄："))
        self.engineer_information["engineer_base_salary"] = float(input("请输入新的基本工资："))
        self.engineer_information["engineer_performance"] = float(input("请输入新的绩效："))
        self.engineer_information["engineer_workday"] = float(input("请输入新的月有效工作天数："))
        self.engineer_information["engineer_InsuranceFee"] = float(input("请输入新的月保险费："))
        print("修改完毕！")

    #功能4：更新部分信息
    def update_partial_information(self):
        print("请选择修改的内容：\n1.编号\n2.姓名\n3.性别\n4.工龄\n5.基本工资\n6.绩效\n7.月有效工作天数\n8.月保险费")
        an = "y"
        while an == "y" or an == "Y":
            update = input("请输入修改项：")
            if update == "1":
                self.engineer_information["engineer_id"] = input("请输入新的编号:")
            elif update == "2":
                self.engineer_information["engineer_name"] = input("请输入新的姓名：")
            elif update == "3":
                self.engineer_information["engineer_sex"] = input("请输入新的性别：")
            elif update == "4":
                self.engineer_information["engineer_work_year"] = int(input("请输入新的工龄："))
            elif update == "5":
                self.engineer_information["engineer_base_salary"] = float(input("请输入新的基本工资："))
            elif update == "6":
                self.engineer_information["engineer_performance"] = float(input("请输入新的绩效："))
            elif update == "7":
                self.engineer_information["engineer_workday"] = float(input("请输入新的月有效工作天数："))
            elif update == "8":
                self.engineer_information["engineer_InsuranceFee"] = float(input("请输入新的月保险费："))
            an=input("是否继续修改？(y/n)")
        else:
            print("修改完毕！")

    # 功能5：计算工程师薪资，并输出
    def calculate_salary(self):
        print("计算薪资:")
        self.engineer_information["engineer_foodfee"] = float(input("请输入每日餐补:"))
        self.engineer_information["engineer_befitmonth"] = float(input("请输入月效益："))
        self.engineer_information["totalsalary"] = (self.engineer_information["engineer_base_salary"] + self.engineer_information["engineer_performance"] +self.engineer_information["engineer_foodfee"] * self.engineer_information["engineer_workday"] +self.engineer_information["engineer_befitmonth"] * self.engineer_information["engineer_work_year"] / 100) * 0.9 - self.engineer_information["engineer_InsuranceFee"]
        print("计算结果：")
        print("---------------------------------------------------------------")
        print("编号:%s\t|姓名:%s\t|本月薪资:%.2f" % (self.engineer_information["engineer_id"], self.engineer_information["engineer_name"],self.engineer_information["totalsalary"]))
        print("---------------------------------------------------------------")

# 功能8：输出信息
    def output_all_information(self):
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
        print("每日餐补:", self.engineer_information["engineer_foodfee"])
        print("月效益:", self.engineer_information["engineer_befitmonth"])
        print("本月薪资:", self.engineer_information["totalsalary"])
        print("-----------------------------------")

    #功能9：清空工程师信息
    def clear_information(self):
        #self.engineer_information.clear()
        self.init_data()
        print("数据清空完毕！")

    #初始化、清空数据
    def init_data(self):
        self.engineer_information["engineer_id"] = "1"
        self.engineer_information["engineer_name"] = ""
        self.engineer_information["engineer_sex"] = "男"
        self.engineer_information["engineer_work_year"] = 1
        self.engineer_information["engineer_base_salary"] = 0.0
        self.engineer_information["engineer_performance"] = 0.0
        self.engineer_information["engineer_workday"] = 0
        self.engineer_information["engineer_InsuranceFee"] = 0.0
        self.engineer_information["engineer_foodfee"] = 0.0
        self.engineer_information["engineer_befitmonth"] = 0.0
        self.engineer_information["totalsalary"] = 0.0

if __name__=="__main__":
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
