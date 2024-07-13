class Student:
    def __init__(self,name,id):
        self.name =name
        self.id = id
    def showdetails(self):
        print(f"The Name Of Student is {self.name} and his ID is {self.id}")
class Programmer(Student):
    def __init__(self,name,id,lang):
     super().__init__(name,id)#this is used to call the constructor of the parent class
     self.lang = lang
    def programmerdetails(self):
       print(f"The Programmer {self.name} and his id {self.id} and language {self.lang}")

s1=Student("Prince",4643)
s1.showdetails()
p1=Programmer("Prince",4643,"python")
p1.programmerdetails()
