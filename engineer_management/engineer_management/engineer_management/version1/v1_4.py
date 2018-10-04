#v1_4：判断功能更加完善(按照字符串判断),并写在独立函数中
def menu():
    print("1.输入软件测试工程师资料")
    print("2.删除指定测试工程师资料")
    print("3.查询软件测试工程师资料")
    print("4.修改软件测试工程师资料")
    print("5.计算测试工程师的月薪水")
    print("6.保存新添加的工程师资料")
    print("7.对测试工程师信息排序(1 编号升序,2 姓名升序,3 工龄降序)")
    print("8.输出所有测试工程师信息")
    print("9.清空所有测试工程师数据")
    print("10.输出软件测试工程师数据表")
    print("11.从文件重新导入测试工程师数据")
    print("0.结束")
    select_id = input("请输入您的选择：")
    return  select_id

def decide_menu(sid):
    list1 = list(range(0, 12))
    for i in list1:
        if sid == str(i):
            print("您选择的是:", sid)
            break
    else:
        print("输入错误!")

if __name__=="__main__":
    sid=menu()
    decide_menu(sid)

