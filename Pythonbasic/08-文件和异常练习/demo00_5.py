#学习带有参数的异常:python3.6不支持此语法

#用户自定义异常
class CustomError(ValueError):
    print("这是一个用户自定义的异常！")

raise CustomError
