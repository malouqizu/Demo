#编写一个用户自定义异常，当用户输入的文本长度小于6个字符时，抛出这个异常
class CustExcp(Exception):
    pass

try:
    i=input("Enter the text:")
    if len(i)<6:
        raise CustExcp()
except CustExcp:
    print("CustomException:Expected length at least 6!")