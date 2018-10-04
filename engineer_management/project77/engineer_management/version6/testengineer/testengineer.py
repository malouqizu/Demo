#2、可以输入多个工程师的信息
import copy
import csv

class Testengineer():
    def __init__(self):
        #存储输入的每个工程师信息
        self.enginfor=dict()
        #暂存每个工程师信息准备插入到list1当中
        #创建一个字典用于deepcopy()操作
        self.dict1=dict()
        #存储所有工程师信息，每个元素为一个字典
        self.list1=list()
        # 工程师信息初始化
        self.init_data()
        #记录总共人数
        self.engnum=0
        #启动时直接导入文件中的数据
        self.import_data()

    #功能1，输入软件测试工程师资料信息
    def input_enginfro(self):
        print(self.engnum)
        an1='y'
        while an1=='y' or an1=='Y':
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
            an1=input("是否继续输入？（y/n）")
        else:
            print("软件测试工程师信息录入结束！")
        self.promt_save()

    #功能1，输出软件测试工程师资料信息
    def output_enginfro(self):
        print("-------------------------------")
        print("工程师的所有信息如下：")
        for ls in self.list1:
            print("编号：", ls['engineer_id'])
            print("姓名：", ls['engineer_name'])
            print("性别：", ls['engineer_sex'])
            print("工龄：", ls['engineer_workyear'])
            print("基本工资：", ls['engineer_basesalary'])
            print("绩效：", ls['engineer_performance'])
            print("月有效天数：", ls['engineer_workday'])
            print("月保险金：", ls['engineer_insurance'])
            print("-------------------------------")

    #功能2，删除指定工程师资料
    def delet_enginfor(self):
        an2='y'
        while an2=='y' or an2=='Y':
            confirm2=input("确定要删除指定工程师资料？（y/n）")
            if confirm2=='y' or confirm2=='Y':
                nameid=input("请输入要删除工程师的编号或者姓名：")
                for ls in self.list1:
                    if ls['engineer_id']==nameid or ls['engineer_name']==nameid:
                        self.list1.remove(ls)
                        break
            an2=input("是否要继续删除指定工程师资料？（y/n）")
        print(self.list1)
        self.promt_save()

    #功能2，删除指定工程师资料
    def delet_enginfor1(self):
        an2='y'
        while an2 in ('y','Y'):
            nameid = input("请输入要删除工程师的编号或者姓名：")
            for ls in self.list1:
                if nameid in (ls['engineer_id'],ls['engineer_name']):
                    confirm2 = input("确定要删除指定工程师资料？（y/n）")
                    if confirm2 in ('y','Y'):
                        i=self.list1.index(ls)
                        del self.list1[i]
                        print(ls['engineer_name'],"工程师信息删除成功！")
                        break
            else:
                print("指定工程师信息没有找到！")
            an2=input("是否要继续删除指定工程师信息？（y/n）")
        self.promt_save()

    #功能3，查询软件测试工程师资料
    def query_enginfor(self):
        print("查询软件工程师资料")
        an3='y'
        while an3 in ('y','Y'):
            namaid3=input("请输入工程师的姓名或者编号：")
            for ls in self.list1:
                if namaid3 in (ls['engineer_id'],ls['engineer_name']):
                    print("工程师信息如下：")
                    print("-------------------------------")
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
                    break
            else:
                print("要查询的工程师不存在！")
            an3=input("是否要继续查询？（y/n）")

    # 功能4，修改工程师信息
    def update_enginfor(self):
        an4='y'
        while an4 in ('y','Y'):
            print("1：修改部分信息\t2：修改全部信息")
            op1=input("请选择：")
            if op1=='1':
                confirm4=input("确定要修改部分信息？（y/n）")
                if confirm4 in ('y','Y'):
                    self.update_partial_enginfor()
                else:
                    print("取消修改部分信息！")
            elif op1=='2':
                confirm4=input("确定要修改全部信息？（y/n）")
                if confirm4 in ('y','Y'):
                    self.update_all_enginfor()
                else:
                    print("取消修改全部信息！")
            an4=input("是否继续修改信息？（y/n）")
        self.promt_save()

    #功能4，修改工程师全部信息
    def update_all_enginfor(self):
        an41='y'
        while an41 in ('y','Y'):
            nameid=input("请输入要更新工程师的编号或者姓名：")
            for ls in self.list1:
                if nameid in (ls['engineer_id'], ls['engineer_name']):
                    confirm41 = input("确定要更新指定工程师全部资料？（y/n）")
                    if confirm41 in ('y', 'Y'):
                        i = self.list1.index(ls)
                        print("-------------------------------")
                        print("更新工程师全部资料：")
                        self.list1[i]['engineer_id'] = input("请输入新的编号：")
                        self.list1[i]['engineer_name'] = input("请输入新的姓名：")
                        self.list1[i]['engineer_sex'] = input("请输入新的性别：")
                        self.list1[i]['engineer_workyear'] = int(input("请输入新的工龄："))
                        self.list1[i]['engineer_basesalary'] = float(input("请输入新的基本工资："))
                        self.list1[i]['engineer_performance'] = float(input("请输入新的绩效："))
                        self.list1[i]['engineer_workday'] = int(input("请输入新的月有效天数："))
                        self.list1[i]['engineer_insurance'] = float(input("请输入新的月保险金："))
                        self.update_other(i)
                        print("-------------------------------")
                        print(self.list1[i]['engineer_name'], "工程师信息全部更新成功！")
                        break
            else:
                print("指定需要更新信息的工程师没有找到！")
            an41 = input("是否要继续更新指定工程师信息？（y/n）")
        print(self.list1)

    #功能4，修改工程师部分信息
    def update_partial_enginfor(self):
        an42 = 'y'
        while an42 in ('y', 'Y'):
            nameid = input("请输入要更新工程师的编号或者姓名：")
            for ls in self.list1:
                if nameid in (ls['engineer_id'], ls['engineer_name']):
                    confirm42 = input("确定要更新指定工程师部分资料？（y/n）")
                    if confirm42 in ('y', 'Y'):
                        i = self.list1.index(ls)
                        print("-------------------------------")
                        print("更新工程师部分资料：")
                        print("请选择修改的内容：\n1.编号\t2.姓名\t3.性别\t4.工龄\t5.基本工资\t6.绩效\t7.月有效工作天数\t8.月保险费")
                        upd = input("请选择：")
                        if upd == '1':
                            self.list1[i]['engineer_id'] = input("请输入新的编号：")
                        elif upd == '2':
                            self.list1[i]['engineer_name'] = input("请输入新的姓名：")
                        elif upd == '3':
                            self.list1[i]['engineer_sex'] = input("请输入新的性别：")
                        elif upd == '4':
                            self.list1[i]['engineer_workyear'] = int(input("请输入新的工龄："))
                        elif upd == '5':
                            self.list1[i]['engineer_basesalary'] = float(input("请输入新的基本工资："))
                            self.update_other(i)
                        elif upd == '6':
                            self.list1[i]['engineer_performance'] = float(input("请输入新的绩效："))
                            self.update_other(i)
                            self.update_other(i)
                        elif upd == '7':
                            self.list1[i]['engineer_workday'] = int(input("请输入新的月有效天数："))
                            self.update_other(i)
                        elif upd == '8':
                            self.list1[i]['engineer_insurance'] = float(input("请输入新的月保险金："))
                            self.update_other(i)
                        print("-------------------------------")
                        print(self.list1[i]['engineer_name'], "工程师部分信息更新成功！")
                        break
            else:
                print("指定需要更新信息的工程师没有找到！")
            an42 = input("是否要继续更新指定工程师信息？（y/n）")
        print(self.list1)

    def update_other(self,i):
        print("基本信息修改完毕，需要重新计算该工程师信息！")
        self.list1[i]["engineer_foodfee"] = 0.0
        self.list1[i]["engineer_befitmonth"] = 0.0
        self.list1[i]["total_salary"] = 0.0

    #功能5，计算软件测试工程师工资
    #要求输入餐补、月效益，然后计算薪资，并显示薪资
    #总薪资＝（基本工资＋月绩效+餐补╳月有效工作日天数＋月效益╳工龄÷100）╳0.9－月保险金
    def calculate_salary(self):
        an5='y'
        while an5 in ('y','Y'):
            print("计算薪资")
            nameid = input("请输入工程师的编号或者姓名：")
            for ls in self.list1:
                if nameid in (ls['engineer_id'], ls['engineer_name']):
                    i=self.list1.index(ls)
                    if float(ls['engineer_foodfee']) == 0.0:
                        self.list1[i]['engineer_foodfee'] = float(input("请输入餐补："))
                    if float(ls['engineer_befitmonth']) == 0.0:
                        self.list1[i]['engineer_befitmonth'] = float(input("请输入月效益："))
                    self.list1[i]['total_salary'] = (float(self.list1[i]['engineer_basesalary']) +
                                                     float(self.list1[i]['engineer_performance']) +
                                                     float(self.list1[i]['engineer_foodfee']) *
                                                     float(self.list1[i]['engineer_workday']) +
                                                     float(self.list1[i]['engineer_befitmonth']) *
                                                     float(self.list1[i]['engineer_workyear']))* 0.9 - \
                                                     float(self.list1[i]['engineer_insurance'])
                    break
            else:
                print("未找到该工程师信息！")
            an5=input("是否要继续计算工程师薪资？（y/n）")
        print(self.list1)
        self.promt_save()

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
                self.engforfile.write("个工程师信息:")
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

    #信息修改之后，提示是否需要保存
    def promt_save(self):
        an=input("工程师信息已经更新，请及时保存！是否保存？（y/n）")
        if an in ('y','Y'):
            self.save_engifro_txtf()
            print("信息保存成功！")
        else:
            print("信息更新后尚未保存！")

    # 功能6，保存信息到excel文件
    def save_enginfor_to_excel(self):
        pass

    #功能7，工程师信息排序
    def sort_enginfor(self):
        tempist_1=copy.deepcopy(self.list1)
        tempist_2=copy.deepcopy(self.list1)
        tempist_3=copy.deepcopy(self.list1)
        tempist1=list()
        tempist2=list()
        tempist3=list()
        qurList1=list()
        qurList2=list()
        qurList3=list()
        an7='y'
        while an7 in ('y','Y'):
            print("对工程师进行排序")
            qur=input("(1)编号升序\t(2)姓名升序\t(3)工龄降序:")
            if qur == '1':
                i=0
                for ls in tempist_1:
                    tempist1.insert(i,ls['engineer_id'])
                    tempist1.sort()
                for q in tempist1:
                    for ls in tempist_1:
                        if q == ls['engineer_id']:
                            qurList1.append(ls)
                            tempist_1.remove(ls)
                for ls in qurList1:
                    print(ls)
            elif qur == '2':
                i = 0
                for ls in tempist_2:
                    tempist2.insert(i, ls['engineer_name'])
                    tempist2.sort()
                for q in tempist2:
                    for ls in tempist_2:
                        if q == ls['engineer_name']:
                            qurList2.append(ls)
                            tempist_2.remove(ls)
                for ls in qurList2:
                    print(ls)
            elif qur == '3':
                i = 0
                for ls in tempist_3:
                    tempist3.insert(i, ls['engineer_workyear'])
                    tempist3.sort()
                    tempist3.reverse()
                print(tempist3)
                for q in tempist3:
                    for ls in tempist_3:
                        if q == ls['engineer_workyear']:
                            qurList3.append(ls)
                            tempist_3.remove(ls)
                for ls in qurList3:
                    print(ls)
            else:
                print("请输入正确的排序信息！")
            an7=input("是否继续排序？（y/n）")

    ##功能7，工程师信息排序
    def sort_enginfor1(self):
        an7='y'
        while an7 in ('y','Y'):
            print("对工程师进行排序")
            qur=input("(1)编号升序\t(2)姓名升序\t(3)工龄降序:")
            if qur == '1':
                self.sort_id_enginfor()
            elif qur == '2':
                self.sort_name_enginfor()
            elif qur == '3':
                self.sort_workyear_enginfor()
            else:
                print("请输入正确的排序信息！")
            an7=input("是否继续排序？（y/n）")

    def sort_id_enginfor(self):
        templist_id = copy.deepcopy(self.list1)
        templistid = list()
        qurListid = list()
        i = 0
        for ls in templist_id:
            templistid.insert(i, ls['engineer_id'])
            templistid.sort()
        for q in templistid:
            for ls in templist_id:
                if q == ls['engineer_id']:
                    qurListid.append(ls)
                    templist_id.remove(ls)
        for ls in qurListid:
            print(ls)

    def sort_name_enginfor(self):
        templist_name = copy.deepcopy(self.list1)
        templistname = list()
        qurListname = list()
        i = 0
        for ls in templist_name:
            templistname.insert(i, ls['engineer_name'])
            templistname.sort()
        for q in templistname:
            for ls in templist_name:
                if q == ls['engineer_name']:
                    qurListname.append(ls)
                    templist_name.remove(ls)
        for ls in qurListname:
            print(ls)

    def sort_workyear_enginfor(self):
        templist_wy = copy.deepcopy(self.list1)
        templistwy = list()
        qurListwy = list()
        i = 0
        for ls in templist_wy:
            templistwy.insert(i, ls['engineer_workyear'])
            templistwy.sort()
            templistwy.reverse()
        print(templistwy)
        for q in templistwy:
            for ls in templist_wy:
                if q == ls['engineer_workyear']:
                    qurListwy.append(ls)
                    templist_wy.remove(ls)
        for ls in qurListwy:
            print(ls)

    #功能8，输出工程师信息
    def output_all_enginfor(self):
        if len(self.list1)>0:
            print("已存在的信息如下：")
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
            print("没有可输出的信息！")

    #功能9，清空工程师信息
    def clear_enginfor(self):
        # del self.enginfor
        self.list1.clear()
        print("数据清空完毕！")

    #功能10，输出工程师为数据表
    def exp_enginfor_for_csv(self):
        excelfile="E:/demo/Python/project77/engineer_management/engineer.csv"
        objfile=open(excelfile,'w+',newline = "")
        csv_writer=csv.writer(objfile, dialect="excel")
        firstline=['engineer_id','engineer_name','engineer_sex','engineer_workyear',
                   'engineer_basesalary','engineer_performance','engineer_workday',
                   'engineer_insurance','engineer_foodfee','engineer_befitmonth',
                   'total_salary']
        csv_writer.writerow(firstline)
        templist=list()
        for ls in self.list1:
            for v in ls.values():
                templist.append(v)
            csv_writer.writerow(templist)
            templist.clear()
        objfile.close()

    # 功能10：版本6.1实现，表格形式输出所有工程师信息
    def grid_output(self):
        i=len(self.list1)
        if i !=0:
            print("                                                                  软件测试工程师信息表")
            print("-------------------------------------------------------------------------------------------------------------------------------------------------")
            print("|\t编号\t|\t姓名\t|\t性别\t|\t工龄\t|\t基本工资\t|\t绩效\t|\t工作天数\t|\t保险\t|\t餐补\t|\t月效益\t|\t本月薪资\t|")
            print("-------------------------------------------------------------------------------------------------------------------------------------------------")

            for infor in self.list1:
                print("|\t",infor["engineer_id"],"\t|\t",infor["engineer_name"],"\t|\t",infor["engineer_sex"],"\t|\t",infor["engineer_workyear"],"\t\t|\t",infor["engineer_basesalary"],"\t\t|\t",infor["engineer_performance"],"\t|\t",infor["engineer_workday"],"\t\t|\t",infor["engineer_insurance"],"\t|\t",infor["engineer_foodfee"],"\t|\t",infor["engineer_befitmonth"],"\t|\t",infor["total_salary"],"\t|")
                print(  "-------------------------------------------------------------------------------------------------------------------------------------------------")
        else:
            print("没有可输出的信息！")

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
        if self.engnum>0:
            i = 0
            while i<self.lines-1:
                list3=list2[i:i+13]
                j=2
                while j<13:
                    str3=list3[j].strip("\n")
                    # print(str3)
                    # print(str3.split(":"))
                    # print(str3.split(":")[0])
                    # print(str3.split(":")[1])
                    self.enginfor[str3.split(":")[0]]=str3.split(":")[1]
                    j=j+1
                self.dict1=copy.deepcopy(self.enginfor)
                num=len(self.list1)
                self.list1.insert(num, self.dict1)
                i=i+13
                print(self.enginfor)
            print(self.list1)
            print("\n")
        else:
            print("目前不存在任何软件测试工程师资料信息！")
        self.engforfile.close()

    # 功能11，从文件重新导入测试工程师数据
    def import_data_from_excel(self):
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
    t=Testengineer()
    #t.input_enginfro()
    #t.update_all_enginfor()
    #t.delet_enginfor()
    t.output_enginfro()
    #t.save_engifro_txtf()
    #t.calculate_salary()
    #t.query_enginfor()
    #t.sort_enginfor()
    #t.sort_enginfor1()
    #t.exp_enginfor_for_csv()
    t.grid_output()
