'''
V1.0版本
软件测试工程师管理信息系统
本版本能够打印用户选择菜单，并让用户选择菜单。
菜单共有12项,包括：
1.输入软件测试工程师资料
2.删除指定测试工程师资料
3.查询软件测试工程师资料
4.修改软件测试工程师资料
5.计算测试工程师的月薪水
6.保存新添加的工程师资料
7.对测试工程师信息排序(1 编号升序,2 姓名升序,3 工龄降序)
8.输出所有测试工程师信息
9.清空所有测试工程师数据
10.输出软件测试工程师数据表
11.从文件重新导入测试工程师数据
0.结束
'''
#v1_1：单条语句实现
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
select_id=input("请输入您的选择：")
print("您选择的是:",select_id)