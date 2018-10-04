'''
版本3,实现功能5，计算软件测试工程师工资。
要求输入餐补、月效益，然后计算薪资，并显示薪资
薪资计算公式：
总薪资＝（基本工资＋月绩效+餐补╳月有效工作日天数＋月效益╳工龄÷100）╳0.9－月保险金
'''
#v3_1
#打印菜单
def menu():
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
#判断菜单选择是否正确
def decide_menu(sid):
    list1 = list(range(0, 12))
    for i in list1:
        if sid == str(i):
            print("您选择的是:", sid)
            break
    else:
        print("输入错误!")

# 输入信息
def input_information():
    engineer_information = dict()
    print("-------------------------------")
    print("请输入软件测试工程师的信息:")
    engineer_information["engineer_id"] = input("请输入编号:")
    engineer_information["engineer_name"] = input("请输入姓名：")
    engineer_information["engineer_sex"] = input("请输入性别：")
    engineer_information["engineer_work_year"] = int(input("请输入工龄："))
    engineer_information["engineer_base_salary"] = float(input("请输入基本工资："))
    engineer_information["engineer_performance"] = float(input("请输入绩效："))
    engineer_information["engineer_workday"] = float(input("请输入月有效工作天数："))
    engineer_information["engineer_insurancefee"] = float(input("请输入月保险费："))
    return engineer_information

#输出信息
def output_information(engineer_infor):
    print("-----------------------------------")
    print("输入的工程师信息如下：")
    print("编号:", engineer_infor["engineer_id"])
    print("姓名:", engineer_infor["engineer_name"])
    print("性别:", engineer_infor["engineer_sex"])
    print("工龄:", engineer_infor["engineer_work_year"])
    print("基本工资:", engineer_infor["engineer_base_salary"])
    print("绩效:", engineer_infor["engineer_performance"])
    print("月有效工作天数:", engineer_infor["engineer_workday"])
    print("保险费:", engineer_infor["engineer_insurancefee"])
    print("-----------------------------------")

#功能5：计算工程师薪资，并输出
def calculate_salary(engineer_infor):
    print("计算薪资:")
    engineer_infor["engineer_foodfee"] = float(input("请输入每日餐补:"))
    engineer_infor["engineer_befitmonth"] = float(input("请输入月效益："))
    engineer_infor["TotalSalary"] = (engineer_infor["engineer_base_salary"] +engineer_infor["engineer_performance"]+ engineer_infor["engineer_foodfee"] *engineer_infor["engineer_workday"] + engineer_infor["engineer_befitmonth"] * engineer_infor["engineer_work_year"] / 100) * 0.9 -  engineer_infor["engineer_insurancefee"]
    print("计算结果：")
    print("---------------------------------------------------------------")
    print("编号:",engineer_infor["engineer_id"],"\t|姓名:" ,engineer_infor["engineer_name"],"\t|本月薪资" ,engineer_infor["TotalSalary"])
    print("---------------------------------------------------------------")

if __name__=="__main__":
    answer = "y"
    while answer == "y" or answer == "Y":
        nofun=("2","3","4","6","7","8","9","10","11","0")
        sid=menu()
        decide_menu(sid)
        if sid=="1":
            engineer_infor = input_information()
            output_information(engineer_infor)
        elif sid=="5":
            calculate_salary(engineer_infor)
        elif sid in nofun:
            print("功能未实现！")
        answer = input("是否继续(y/n)?")
    else:
        print("程序结束!")
