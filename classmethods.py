class Student:
    university="Amity University"
    def __init__(self,name,rollno,address):
        self.name = name
        self.rollno = rollno
        self.address = address
    def showdetails(self):
        print(f"The Student of {self.address} whose name is {self.name} studying in {self.university} and his University  rollno is {self.rollno}")
    # def changeclass(cls,newclass):#It behaves like normal method it change only instance
    #     cls.university = newclass
    @classmethod
    def changeclass(cls,newclass):#It is class method it will change the  class variable
        cls.university = newclass

s1=Student("Prince",2242000396,"Etah")
s1.showdetails()
s1.changeclass("GLA University")
s1.showdetails()
print(Student.university)
s2=Student("Nikhil Chahar",2242000347,"Agra")
s2.showdetails()
    
