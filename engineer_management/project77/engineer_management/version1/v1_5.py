#v1_5：可以循环输入
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

if __name__=="__main__":
    answer='y'
    while answer=='y' or answer=='Y':
        sid=menu()
        select_menu(sid)
        answer=input("是否要继续？(y/n)")
    else:
        print("程序结束！")


