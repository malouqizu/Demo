import copy

class TestEngineer():
    #构造函数，初始化数据
    def __init__(self):
        #存储输入的每个工程师信息
        self.engineer_information = dict()
        #暂存新添加的每个工程师信息，准备插入到list2中
        self.list1 = list()
        #存储所有工程师信息，每个元素为一个字典
        self.list2 = list()
        #工程师信息初始化
        self.init_data()
        #self.num=0
        # 记录总共人数
        self.h=0
        #启动时直接导入文件中的数据
        self.import_data()

    # 功能1：在导入信息基础上，输入多个工程师信息
    def input_information(self):
        print("-------------------------------")
        an2="y"
        while an2 in("y","Y"):
            self.h += 1
            print("请输入第%d个软件测试工程师的信息:"%self.h)
            #self.engineer_information["num"]=self.num
            self.engineer_information["engineer_id"] = input("请输入编号:")
            #for m in self.list2:
            #    if m["engineer_id"]==self.engineer_information["engineer_id"]:
            #        self.engineer_information["engineer_id"] = input("请重新输入编号:")
            self.engineer_information["engineer_name"] = input("请输入姓名：")
            self.engineer_information["engineer_sex"] = input("请输入性别：")
            self.engineer_information["engineer_work_year"] = input("请输入工龄：")
            self.engineer_information["engineer_base_salary"] = input("请输入基本工资：")
            self.engineer_information["engineer_performance"] = input("请输入绩效：")
            self.engineer_information["engineer_workday"] = input("请输入月有效工作天数：")
            self.engineer_information["engineer_InsuranceFee"] = input("请输入月保险费：")
            self.engineer_information["engineer_foodfee"]=0.00
            self.engineer_information["engineer_foodfee"] = 0.00
            self.engineer_information["total_salary"] = 0.00
            #把字典深复制到列表1中（list1转换为字典）
            self.list1=copy.deepcopy(self.engineer_information)
            #self.num=len(self.list2)
            #self.list2.insert(self.num,self.list1)
            #print(self.h)
            # 将列表1插入到列表2指定位置
            self.list2.insert(self.h, self.list1)
            #print("list1:",self.list1)
            #print("list2:",self.list2)
            an2=input("是否继续输入？(y/n)")

    #功能1：输出工程师信息
    def output_information(self):
        print("-----------------------------------")
        print("输入的工程师的信息如下：")
        for infor in self.list2:
            print("编号:", infor["engineer_id"])
            print("姓名:", infor["engineer_name"])
            print("性别:", infor["engineer_sex"])
            print("工龄:", infor["engineer_work_year"])
            print("基本工资:", infor["engineer_base_salary"])
            print("绩效:", infor["engineer_performance"])
            print("月有效工作天数:", infor["engineer_workday"])
            print("保险费:", infor["engineer_InsuranceFee"])
            print("-----------------------------------")

    #功能2：删除指定工程师信息
    def del_information(self):
        an4="y"
        while an4 in("Y","y"):
            del_infor=input("请输入要删除的工程师编号或姓名:")
            for infor in self.list2:
                if del_infor in (infor["engineer_id"],infor["engineer_name"]):
                    confirm1=input("是否真的删除指定工程师信息？(y/n)")
                    if confirm1 in("Y","y"):
                        i=self.list2.index(infor)
                        del self.list2[i]
                        print("数据删除成功！")
                        print("list2:", self.list2)
                    break
            else:
                print("没有找到指定的工程师编号或姓名！")
            an4=input("是否继续删除？(y/n)")

    #功能4：修改工程师所有信息
    def update_all_information(self):
        print("-------------------------------")
        print("请修改软件测试工程师的信息:")
        self.engineer_information["engineer_id"] = input("请输入新的编号:")
        self.engineer_information["engineer_name"] = input("请输入新的姓名：")
        self.engineer_information["engineer_sex"] = input("请输入新的性别：")
        self.engineer_information["engineer_work_year"] = input("请输入新的工龄：")
        self.engineer_information["engineer_base_salary"] = input("请输入新的基本工资：")
        self.engineer_information["engineer_performance"] = input("请输入新的绩效：")
        self.engineer_information["engineer_workday"] = input("请输入新的月有效工作天数：")
        self.engineer_information["engineer_InsuranceFee"] = input("请输入新的月保险费：")
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
                self.engineer_information["engineer_work_year"] = input("请输入新的工龄：")
            elif update == "5":
                self.engineer_information["engineer_base_salary"] = input("请输入新的基本工资：")
            elif update == "6":
                self.engineer_information["engineer_performance"] = input("请输入新的绩效：")
            elif update == "7":
                self.engineer_information["engineer_workday"] = input("请输入新的月有效工作天数：")
            elif update == "8":
                self.engineer_information["engineer_InsuranceFee"] = input("请输入新的月保险费：")
            an=input("是否继续修改？(y/n)")
        else:
            print("修改完毕！")

    # 功能5：计算指定工程师薪资，并输出
    def calculate_salary(self):
        print("计算薪资:")
        an3="y"
        while an3 in ("Y","y"):
            engineer=input("请输入工程师的编号或姓名:")
            for person in self.list2:
                if engineer==person["engineer_id"] or engineer==person["engineer_name"]:
                    person["engineer_foodfee"]=float(input("请输入每日餐补:"))
                    person["engineer_befitmonth"] = float(input("请输入月效益："))
                    person["total_salary"] = (float(person["engineer_base_salary"]) + float(person["engineer_performance"]) +person["engineer_foodfee"] * int(person["engineer_workday"]) +person["engineer_befitmonth"] * int(person["engineer_work_year"]) / 100) * 0.9 - float(person["engineer_InsuranceFee"])
                    print("计算结果：")
                    print("---------------------------------------------------------------")
                    print("编号:%s\t|姓名:%s\t|本月薪资:%.2f" % (person["engineer_id"], person["engineer_name"],person["total_salary"]))
                    print("---------------------------------------------------------------")
                    # 把字典深复制到列表1中（list1转换为字典）
                    self.list1 = copy.deepcopy(person)
                    # 将列表1插入到列表2指定位置
                    self.pos = self.list2.index(person)
                    self.list2.remove(person)
                    self.list2.insert(self.pos, self.list1)
                    print("list1:", self.list1)
                    print("list2:", self.list2)
                    break
            else:
                print("指定的编号或姓名不存在！")

            an3 = input("是否继续计算薪资？(y/n)")

    #功能6，保存信息到文件
    def save_information(self):
        file=open("E:\mypythonpj\engineer.txt","w+")
        j=1
        for self.f in self.list2:
            #print(self.f)
            file.write("--------------------------\n")
            file.write("第%d个工程师信息:\n"%j)
            for key,value in self.f.items():
                file.write(key)
                file.write(":")
                file.write(str(value))
                file.write("\n")
            j+=1
        file.close()
        print("数据保存成功！")

    # 功能8：输出信息
    def output_all_information(self):
        print("-----------------------------------")
        print("输入的工程师的信息如下：")
        for infor in self.list2:
            print("编号:", infor["engineer_id"])
            print("姓名:", infor["engineer_name"])
            print("性别:", infor["engineer_sex"])
            print("工龄:", infor["engineer_work_year"])
            print("基本工资:", infor["engineer_base_salary"])
            print("绩效:", infor["engineer_performance"])
            print("月有效工作天数:", infor["engineer_workday"])
            print("保险费:", infor["engineer_InsuranceFee"])
            print("每日餐补:", infor["engineer_foodfee"])
            print("月效益:", infor["engineer_befitmonth"])
            print("本月薪资:", infor["total_salary"])
            print("-----------------------------------")

    #功能9：清空工程师信息
    def clear_information(self):
        #self.engineer_information.clear()
        self.init_data()
        print("数据清空完毕！")

    #功能11，重新从文件导入数据
    def import_data(self):
        file = open("E:\mypythonpj\engineer.txt", "w+")
        #读取所有行存在列表中，每行作为列表的一个元素
        listdata=file.readlines()
        #计算总的行数
        k=len(listdata)
        #判断总共几组数据，每个人使用13行
        self.h=int(k/13)
        i=0
        print("共导入%d个工程师信息。"%self.h)
        while i<self.h:
            j = 2  #每组数据的前两行不读，从第三行engineer_id开始读取
            #print("第%d个工程师信息：" % (i+1))
            while j<13:
                #通过索引，读取列表元素，读出每个信息数据
                temp=listdata[j+13*i]
                #分隔每个信息数据，通过冒号分隔键和值，存在templist中
                templist=temp.split(":")
                #取出键
                key=templist[0]
                #取出值
                value=templist[1]
                #去掉值中的“\n”
                value=templist[1].rstrip("\n")
                #存在字典中
                self.engineer_information[key] = value
                j+=1
            #print(self.engineer_information)
            # 把字典深复制到列表1中（list1转换为字典）
            self.list1 = copy.deepcopy(self.engineer_information)
            # 将列表1插入到列表2指定位置
            self.num = len(self.list2)
            self.list2.insert(self.num, self.list1)
            #print("list1:", self.list1)
            #print("list2:", self.list2)
            i+=1

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
        self.engineer_information["total_salary"] = 0.0

