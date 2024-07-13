class Student:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))
    
s1=Student("Prince",10000)
print(s1.name,s1.salary)
string="Nikhil-10000"
# print(string.split("-",1)[0],string.split("-")[1])
e2=Student.fromstr(string)
print(e2.name,e2.salary)