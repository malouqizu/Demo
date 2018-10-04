#v1_4：判断功能更加完善(按照字符串判断),并写在独立函数中
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

def select_menu(sid):
    list1=list(range(0,12))
    for i in list1:
        if sid == str(i):
            print("您输入的选择：",sid)
            break
    else:
        print("选择错误！")

def select_menu1(sid):
    option=['0','1','2','3','4','5','6','7','8','9','10','11']
    if sid in option:
        print("您输入的选择是：", sid)
    else:
        print("选择错误！")

def select_menu2(sid):
    list1=list(range(0,12))
    if int(sid) in list1:
        print("您输入的选择：",sid)
    else:
        print("选择错误！")

def select_menu3(sid):
    option=('0','1','2','3','4','5','6','7','8','9','10','11')
    if sid in option:
        print("您输入的选择是：", sid)
    else:
        print("选择错误！")

def select_menu4(sid):
    tup1=tuple(range(0,12))
    for i in tup1:
        if sid == str(i):
            print("您输入的选择：",sid)
            break
    else:
        print("选择错误！")

def select_menu5(sid):
    tup1 = tuple(range(0, 12))
    tup1 = str(tup1)
    if sid in tup1:
        print("选择正确！")
    else:
        print("选择错误！")

if __name__=="__main__":
    sid=menu()
    select_menu(sid)
