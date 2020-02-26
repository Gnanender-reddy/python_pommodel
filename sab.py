class cal:
    num=100
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("this is executed first")
    def som(self):
        print("lass")
        return self.a+self.b+self.num


c=cal(2,3)
print(c.som())