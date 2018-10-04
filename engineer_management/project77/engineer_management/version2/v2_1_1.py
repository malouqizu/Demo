'''
V2.0版本
实现功能1，提示输入软件测试工程师资料信息，信息包括：
编号、姓名、性别、工龄、基本工资、绩效、月有效工作天数，月保险金。
并输出相应的信息资料
'''
#v2_1_1
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
    print("您的选择是", select_id)
    return select_id

#选择
def select_menu(sid):
    list1=list(range(0,12))
    for i in list1:
        if sid == str(i):
            select_function(sid)
            break
    else:
        print("选择错误！")

def select_function(sid):
    nofun=['2','3','4','5','6','7','8','9','10','11','0']
    if sid=='1':
        input_enginfro()
    elif sid in nofun:
        print(sid,"功能未实现！")

#功能1，提示输入软件测试工程师资料信息，并输出相应的信息资料
def input_enginfro():
    print("-------------------------------")
    print("请输入软件测试工程师信息:")
    engineer_id=input("编号：")
    engineer_name=input("姓名：")
    engineer_sex=input("性别：")
    engineer_workyear=int(input("工龄："))
    engineer_basesalary=float(input("基本工资："))
    engineer_performance=float(input("绩效："))
    engineer_workday=int(input("月有效天数："))
    engineer_insurance=float(input("月保险金："))

    print("-------------------------------")
    print("输入的工程师信息如下：")
    print("编号：",engineer_id)
    print("姓名：",engineer_name)
    print("性别：",engineer_sex)
    print("工龄：",engineer_workyear)
    print("基本工资：",engineer_basesalary)
    print("绩效：",engineer_performance)
    print("月有效天数：",engineer_workday)
    print("月保险金：",engineer_insurance)

if __name__=="__main__":
    answer='y'
    while answer=='y' or answer=='Y':
        sid=menu()
        select_menu(sid)
        answer=input("是否要继续？(y/n)")
    else:
        print("程序结束！")