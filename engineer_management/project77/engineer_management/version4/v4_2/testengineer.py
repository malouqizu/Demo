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
        self.enginfor['engineer_id'] = input("编号：")
        self.enginfor['engineer_name'] = input("姓名：")
        self.enginfor['engineer_sex'] = input("性别：")
        self.enginfor['engineer_workyear'] = int(input("工龄："))
        self.enginfor['engineer_basesalary'] = float(input("基本工资："))
        self.enginfor['engineer_performance'] = float(input("绩效："))
        self.enginfor['engineer_workday'] = int(input("月有效天数："))
        self.enginfor['engineer_insurance'] = float(input("月保险金："))
        self.enginfor['engineer_foodfee'] = float(input("请输入餐补："))
        self.enginfor['engineer_befitmonth'] = float(input("请输入月效益："))
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
        if self.enginfor['engineer_foodfee'] != 0.0:
            pass
        else:
            self.enginfor['engineer_foodfee'] = float(input("请输入餐补："))
        if self.enginfor['engineer_befitmonth'] != 0.0:
            pass
        else:
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