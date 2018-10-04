#2、可以输入多个工程师的信息
import copy
class Testengineer():
    def __init__(self):
        #存储输入的每一个工程师信息
        self.enginfor=dict()
        #暂存每个工程师信息准备插入到list1当中
        #创建一个字典用于deepcopy()操作
        self.dict1=dict()
        #存储所有工程师信息，元素为字典，每个元素代表一个工程师信息
        self.list1=list()
        # 初始化工程师信息
        self.init_data()
        #用来记录工程师总数
        self.engnum=0
        #直接导入文件中所有工程师的数据
        self.import_data()

    #功能1，输入软件测试工程师资料信息
    def input_enginfro(self):
        print(self.engnum)
        an='y'
        while an=='y' or an=='Y':
            self.engnum = self.engnum + 1
            print("-------------------------------")
            print("输入第",self.engnum,"个工程师信息：")
            self.enginfor['engineer_id'] = input("编号：")
            self.enginfor['engineer_name'] = input("姓名：")
            self.enginfor['engineer_sex'] = input("性别：")
            self.enginfor['engineer_workyear'] = int(input("工龄："))
            self.enginfor['engineer_basesalary'] = float(input("基本工资："))
            self.enginfor['engineer_performance'] = float(input("绩效："))
            self.enginfor['engineer_workday'] = int(input("月有效天数："))
            self.enginfor['engineer_insurance'] = float(input("月保险金："))
            self.dict1=copy.deepcopy(self.enginfor)
            print(self.enginfor)
            print(self.dict1)
            self.list1.insert(self.engnum,self.dict1)
            #print(self.engnum)
            print(self.list1)
            an=input("是否继续输入？（y/n）")
        else:
            print("软件测试工程师信息录入结束！")

    #功能1，输出软件测试工程师资料信息
    def output_enginfro(self):
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
        print("-------------------------------")

    # 功能2，删除工程师信息
    def delet_enginfor(self):
        # del self.enginfor
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
        pass

    #功能6，保存信息到文本文件
    def save_engifro_txtf(self):
        self.file_name = "E:/demo/Python/project77/engineer_management/engineer.txt"
        self.engforfile = open(self.file_name, 'w+')
        print("保存信息到",self.file_name)
        self.engforfile.seek(0)
        if self.engnum>0:
            i=1
            for ls in self.list1:
                self.engforfile.write("--------------------------")
                self.engforfile.write("\n")
                self.engforfile.write("第")
                self.engforfile.write(str(i))
                self.engforfile.write("工程师信息:")
                self.engforfile.write("\n")
                for k, v in ls.items():
                    self.engforfile.write(str(k))
                    self.engforfile.write(":")
                    self.engforfile.write(str(v))
                    self.engforfile.write("\n")
                i=i+1
        else:
            print("请输入软件测试工程师信息！")

        self.engforfile.close()

    #功能8，输出工程师信息
    def output_all_enginfor(self):
        if len(self.list1)>0:
            for ls in self.list1:
                print("-------------------------------")
                print("输入的工程师信息如下：")
                print("编号：", ls['engineer_id'])
                print("姓名：", ls['engineer_name'])
                print("性别：", ls['engineer_sex'])
                print("工龄：", ls['engineer_workyear'])
                print("基本工资：", ls['engineer_basesalary'])
                print("绩效：", ls['engineer_performance'])
                print("月有效天数：", ls['engineer_workday'])
                print("月保险金：", ls['engineer_insurance'])
                print("餐补：", ls['engineer_foodfee'])
                print("月效益：", ls['engineer_befitmonth'])
                print("薪水：", ls['total_salary'])
                print("-------------------------------")
        else:
            print("不存在工程师信息！")

    #功能9，清空工程师信息
    def clear_enginfor(self):
        # del self.enginfor
        self.enginfor.clear()
        self.init_data()

    #功能0，结束
    def over(self):
        pass

    #功能11，从文件重新导入测试工程师数据
    def import_data(self):
        self.file_name = "E:/demo/Python/project77/engineer_management/engineer.txt"
        self.engforfile = open(self.file_name, 'r+')
        list2=self.engforfile.readlines()
        # print(list2)
        self.lines=len(list2)
        # print(self.lines)
        # 因为最后一行在添加时多了一个换行，所以读出来的列表值应该减一
        self.engnum=(self.lines)//13
        # print(self.engnum)
        i=0
        if self.engnum>0:
            while i<self.engnum:
                j=2
                while j<13:
                    templist = list2[j+i*13]
                    tempstr=templist[j].strip("\n")
                    # print(str3)
                    # print(str3.split(":"))
                    # print(str3.split(":")[0])
                    # print(str3.split(":")[1])
                    self.enginfor[tempstr.split(":")[0]]=tempstr.split(":")[1]
                    j=j+1
                self.dict1=copy.deepcopy(self.enginfor)
                num=len(self.list1)
                self.list1.insert(num, self.dict1)
                i=i+1
                print(self.enginfor)
            print(self.list1)
            print("\n")
        else:
            print("目前不存在任何软件测试工程师资料信息！")

        self.engforfile.close()

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
    t=Testengineer()
    t.input_enginfro()
    t.save_engifro_txtf()
