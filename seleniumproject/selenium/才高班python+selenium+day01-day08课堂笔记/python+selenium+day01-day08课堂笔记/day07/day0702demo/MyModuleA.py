class MyOne:
    def first(self):
        str1=input("������3������,�Կո�ָ�:")
        str2=str1.split(" ")
        print(str2)
        return str2

    def second(self):
        data1=input("������1������:")
        return data1

    def third(self):
        f=self.first()
        s=self.second()
        if s in f:
            print("����")
        else:
            print("������")

if __name__=="__main__":
    m=MyOne()
    m.third()