class Count:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    #add函数
    def add(self):
        self.r1=self.x+self.y
        return self.r1

    #计算减法
    def sub(self):
        self.r2=self.x-self.y
        return self.r2
    #mul函数
    def mul(self):
        self.r3=self.x*self.y
        return self.r3

    #div函数
    def div(self):
        self.r4=self.x/self.y
        return self.r4