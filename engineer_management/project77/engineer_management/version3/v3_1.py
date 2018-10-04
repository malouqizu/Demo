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
    print("您的选择是", select_id)
    return select_id

#选择
def select_menu(sid):
    list1=list(range(0,12))
    for i in list1:
        if sid == str(i):
            #select_function(sid)
            break
    else:
        print("选择错误！")

def select_function(sid):
    nofun=['2','3','4','6','7','8','9','10','11','0']
    if sid=='1':
        infro = input_enginfro()
        output_enginfro(infro)
    elif sid in nofun:
        print(sid, "功能未实现！")

#功能1，提示输入软件测试工程师资料信息，并输出相应的信息资料
def input_enginfro():
    enginfor=dict()
    print("-------------------------------")
    print("请输入软件测试工程师信息:")
    enginfor['engineer_id']=input("编号：")
    enginfor['engineer_name']=input("姓名：")
    enginfor['engineer_sex']=input("性别：")
    enginfor['engineer_workyear']=int(input("工龄："))
    enginfor['engineer_basesalary']=float(input("基本工资："))
    enginfor['engineer_performance']=float(input("绩效："))
    enginfor['engineer_workday']=int(input("月有效天数："))
    enginfor['engineer_insurance']=float(input("月保险金："))
    return enginfor

def output_enginfro(enginfor):
    print("-------------------------------")
    print("输入的工程师信息如下：")
    print("编号：",enginfor['engineer_id'])
    print("姓名：",enginfor['engineer_name'])
    print("性别：",enginfor['engineer_sex'])
    print("工龄：",enginfor['engineer_workyear'])
    print("基本工资：",enginfor['engineer_basesalary'])
    print("绩效：",enginfor['engineer_performance'])
    print("月有效天数：",enginfor['engineer_workday'])
    print("月保险金：",enginfor['engineer_insurance'])
    print("-------------------------------")

#功能5，计算软件测试工程师工资
#要求输入餐补、月效益，然后计算薪资，并显示薪资
#总薪资＝（基本工资＋月绩效+餐补╳月有效工作日天数＋月效益╳工龄÷100）╳0.9－月保险金
def calculate_salary(enginfor):
    print("计算软件测试工程师薪资")
    enginfor['engineer_foodfee']=float(input("请输入餐补："))
    enginfor['engineer_befitmonth']=float(input("请输入月效益："))
    enginfor['total_salary']=(enginfor['engineer_basesalary']+enginfor['engineer_performance']+
                              enginfor['engineer_foodfee']*enginfor['engineer_workday']+
                              enginfor['engineer_befitmonth']*enginfor['engineer_workyear'])*0.9-enginfor['engineer_insurance']
    print("薪资：",enginfor['total_salary'])

if __name__=="__main__":
    nofun = ['2', '3', '4', '6', '7', '8', '9', '10', '11', '0']
    answer='y'
    while answer=='y' or answer=='Y':
        sid=menu()
        select_menu(sid)
        if sid == '1':
            infro=input_enginfro()
            output_enginfro(infro)
        elif sid=='5':
            calculate_salary(infro)
        elif sid in nofun:
            print(sid, "功能未实现！")
        answer=input("是否要继续？(y/n)")
    else:
        print("程序结束！")
