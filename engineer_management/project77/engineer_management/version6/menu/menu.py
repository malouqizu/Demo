class Menu():
    def menu(self):
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

        self.select_id = input("请输入您的选择：")
        print("您的选择是", self.select_id)

    # 选择
    def select_menu(self):
        list1 = list(range(0, 12))
        for i in list1:
            if self.select_id == str(i):
                # select_function(sid)
                break
        else:
            print("选择错误！")

    def select_function(self,t):
        nofun=['3','7','10']
        self.t=t
        if self.select_id == '1':
            self.t.input_enginfro()
            self.t.output_enginfro()
        elif self.select_id == '2':
            confirm=input("是否真的要删除工程师信息？（y/n）")
            if confirm=='y' or confirm=='Y':
                self.t.delet_enginfor()
            else:
                print("取消删除操作！")
        elif self.select_id == '4':
            confirm = input("是否真的要修改工程师信息？（y/n）")
            if confirm == 'y' or confirm == 'Y':
                print("1：修改部分信息 2：修改全部信息")
                opt=input("请输入选择：")
                if opt=='1':
                    self.t.update_partial_enginfor()
                elif opt=='2':
                    self.t.update_all_enginfor()
                else:
                    print("选择错误！")
        elif self.select_id == '5':
            if self.t.enginfor['engineer_name'] == "":
                print("请先输入软件测试工程师的资料信息！")
            else:
                self.t.calculate_salary()
        elif self.select_id == '6':
            pass
        elif self.select_id == '8':
            self.t.output_all_enginfor()
        elif self.select_id == '9':
            confirm = input("是否真的要清空工程师信息？（y/n）")
            if confirm == 'y' or confirm == 'Y':
                self.t.clear_enginfor()
            else:
                print("取消清空操作！")
        elif self.select_id == '11':
            pass
        elif self.select_id in nofun:
            print(self.select_id, "功能未实现！")


