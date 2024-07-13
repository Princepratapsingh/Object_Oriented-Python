class Grandfather:
    def __init__(self,grandfathername):
        self.grandfathername = grandfathername

class Father(Grandfather):
    def __init__(self,FatherName,grandfathername):
        super().__init__(grandfathername)
        self.FatherName =FatherName

class Son(Father):
    def __init__(self,sonname,FatherName,grandfathername):
        self.sonname = sonname
        super().__init__(FatherName,grandfathername)
    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.FatherName)
        print("Son name :", self.sonname)
 
 
#  Driver code
s1 = Son('Prince', 'Rinku Singh','VijayPal Singh')
print(s1.grandfathername)
s1.print_name()