#定义Stu类
class Stu:
    def info(self,n,num,*p):
        self.name=n
        self.num=num
        self.other=p
        print("姓名:",self.name)
        print("编号:",self.num)
        self.m=len(self.other)
        if self.m == 0:
            print("其他信息:无")
        else:
            print("其他信息:")
            for item in self.other:
                print(item)
#实例化Stu
xiaoming=Stu()
#调用函数
xiaoming.info("小明","A0001")

#实例化一个xiaohong对象
xiaohong=Stu()
xiaohong.info("小红","A0002","北京","女","13678908765")
