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
        nofun=['3','6','7','10','11']
        self.t=t
        if self.select_id == '1':
            self.t.input_enginfro()
            self.t.output_enginfro()
        elif self.select_id == '2':
            confirm=input("是否真的要删除工程师信息？（y/n）")
            if confirm=='y' or confirm=='Y':
                self.t.delet_enginfor()
            else:
                print("取消删除操作！")
        elif self.select_id == '4':
            confirm = input("是否真的要修改工程师信息？（y/n）")
            if confirm == 'y' or confirm == 'Y':
                print("1：修改部分信息 2：修改全部信息")
                opt=input("请输入选择：")
                if opt=='1':
                    self.t.update_partial_enginfor()
                elif opt=='2':
                    self.t.update_all_enginfor()
                else:
                    print("选择错误！")
        elif self.select_id == '5':
            if self.t.enginfor['engineer_name'] == "":
                print("请先输入软件测试工程师的资料信息！")
            else:
                self.t.calculate_salary()
        elif self.select_id == '8':
            self.t.output_all_enginfor()
        elif self.select_id == '9':
            confirm = input("是否真的要清空工程师信息？（y/n）")
            if confirm == 'y' or confirm == 'Y':
                self.t.clear_enginfor()
            else:
                print("取消清空操作！")
        elif self.select_id in nofun:
            print(self.select_id, "功能未实现！")


class Testengineer():
    def __init__(self):
        self.enginfor=dict()
        self.init_data()

    #功能1.0，输入软件测试工程师资料信息
    def input_enginfro(self):
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

    # 功能1.1，输出软件测试工程师资料信息
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

    #功能2，删除工程师信息
    def delet_enginfor(self):
        #del self.enginfor
        self.enginfor.clear()
        self.init_data()

    #功能4，修改工程师信息
    #功能4.0，修改工程师的全部信息
    def update_all_enginfor(self):
        print("-------------------------------")
        print("更新工程师全部资料：")
        print("编号：", self.enginfor['engineer_id'])
        print("姓名：", self.enginfor['engineer_name'])
        print("性别：", self.enginfor['engineer_sex'])
        print("工龄：", self.enginfor['engineer_workyear'])
        print("基本工资：", self.enginfor['engineer_basesalary'])
        print("绩效：", self.enginfor['engineer_performance'])
        print("月有效天数：", self.enginfor['engineer_workday'])
        print("月保险金：", self.enginfor['engineer_insurance'])
        print("-------------------------------")

    # 功能4.1，修改工程师的全部信息
    def update_partial_enginfor(self):
        print("-------------------------------")
        print("更新工程师部分资料：")
        #print("请选择修改的内容：\n1.编号\t2.姓名\t3.性别\t4.工龄\t5.基本工资\t6.绩效\t7.月有效工作天数\t8.月保险费")
        an='y'
        while an=='y' or an=='Y':
            print("请选择修改的内容：\n1.编号\t2.姓名\t3.性别\t4.工龄\t5.基本工资\t6.绩效\t7.月有效工作天数\t8.月保险费")
            upd=input("请选择：")
            if upd=='1':
                self.enginfor['engineer_id'] = input("编号：")
            elif upd=='2':
                self.enginfor['engineer_name'] = input("姓名：")
            elif upd=='3':
                self.enginfor['engineer_sex'] = input("性别：")
            elif upd=='4':
                self.enginfor['engineer_workyear'] = int(input("工龄："))
            elif upd=='5':
                self.enginfor['engineer_basesalary'] = float(input("基本工资："))
            elif upd=='6':
                self.enginfor['engineer_performance'] = float(input("绩效："))
            elif upd=='7':
                self.enginfor['engineer_workday'] = int(input("月有效天数："))
            elif upd=='8':
                self.enginfor['engineer_insurance'] = float(input("月保险金："))
            an=input("是否要继续进行修改？（y/n）")
        else:
            print("信息更新完毕！")

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

    #功能8，输出工程师信息
    def output_all_enginfor(self):
        print("-------------------------------")
        print("工程师的所有信息如下：")
        print("编号：", self.enginfor['engineer_id'])
        print("姓名：", self.enginfor['engineer_name'])
        print("性别：", self.enginfor['engineer_sex'])
        print("工龄：", self.enginfor['engineer_workyear'])
        print("基本工资：", self.enginfor['engineer_basesalary'])
        print("绩效：", self.enginfor['engineer_performance'])
        print("月有效天数：", self.enginfor['engineer_workday'])
        print("月保险金：", self.enginfor['engineer_insurance'])
        print("餐补：",self.enginfor['engineer_foodfee'])
        print("月效益：",self.enginfor['engineer_befitmonth'])
        print("薪水：",self.enginfor['total_salary'])
        print("-------------------------------")

    #功能9，清空工程师信息
    def clear_enginfor(self):
        # del self.enginfor
        self.enginfor.clear()
        self.init_data()

    #功能0，结束
    def over(self):
        pass

   #初始化软件测试工程师数据
    def init_data(self):
        self.enginfor['engineer_id']="1"
        self.enginfor['engineer_name']=""
        self.enginfor['engineer_sex']="男"
        self.enginfor['engineer_workyear']=0
        self.enginfor['engineer_basesalary']=0.0
        self.enginfor['engineer_performance']=0.0
        self.enginfor['engineer_workday']=0
        self.enginfor['engineer_insurance']=0.0
        self.enginfor['engineer_foodfee']=0.0
        self.enginfor['engineer_befitmonth']=0.0
        self.enginfor['total_salary']=0.0


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

