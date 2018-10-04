#1、编写一个程序，定义一个类，这个类包含两个方法：inputStr()会从
#命令行输入窗口中获取字符串，printStr()会把这个字符串以大写形式
#打印出来。同时使用一个函数来测试这个类方法。
class StrUpper():
    def inputStr(self):
        self.str=input("请输入一个字符串：")

    def printStr(self):
        print(self.str.upper())

s=StrUpper()
s.inputStr()
s.printStr()