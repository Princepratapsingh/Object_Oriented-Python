class Math:
    def __init__(self,num):
        self.num = num
    def addtonum(self,n):
        self.num += n
    @staticmethod
    def add(a,b):
        return a + b

result=Math.add(2,4)
print(result)
a=Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
print(a.add(2,4))