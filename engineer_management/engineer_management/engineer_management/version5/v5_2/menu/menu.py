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
        print("|\t0.结束\t\t\t\t\t\t\t  |")
        print("======================================")
        select_id = input("请输入您的选择：")
        return select_id

    # 判断菜单选择是否正确
    def decide_menu(self,sid):
        list1 = list(range(0, 12))
        for i in list1:
            if sid == str(i):
                print("您选择的是:", sid)
                break
        else:
            print("输入错误!")
    #版本4实现2、4、8、9、0功能，对选择进行相应的判断
    def select_function(self,sid,t):
        nofun = ("3","7", "10")
        self.t = t
        if sid == "1":
            self.t.input_information()
            self.t.output_information()
        #版本4实现：删除工程师信息
        elif sid=="2":
                self.t.del_information()
                #删除信息后,提示保存
                self.t.prompt_save()
        # 版本4实现：修改指定工程师信息
        elif sid=="4":
            self.t.update_information()
            # 修改信息后，提示保存
            self.t.prompt_save()
        #计算薪资
        elif sid == "5":
            self.t.calculate_salary()
            # 计算薪资后，提示保存
            self.t.prompt_save()

        #版本5_2实现,功能6，保存信息到文本文件
        elif sid=="6":
            self.t.save_information()

        #版本4实现：输出所有信息
        elif sid=="8":
            self.t.output_all_information()
        #版本4实现：清空所有信息
        elif sid=="9":
            confirm2=input("是否真的清空工程师信息？(Y/N)")
            if confirm2=="y" or confirm2=="Y":
                self.t.clear_information()
                # 清空数据后，提示保存
                self.t.prompt_save()
            else:
                print(" 取消清空！")

        # 版本5_2实现,功能11，从文件重新导入数据
        elif sid =="11":
            confirm11 = input("是否重新导入工程师信息？(Y/N)")
            if confirm11 == "y" or confirm11 == "Y":
                self.t.import_data()
        elif sid in nofun:
            print("功能未实现！")
