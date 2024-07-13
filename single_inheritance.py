class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showdetails(self):
        print(f"The Name of Employee is {self.name} and his ID is {self.id}")
class Student(Employee):
    def __init__(self,name,id,university):
        super().__init__(name,id)
        self.university = university 
    def showdetails(self):
        print(f"The Name of Student is {self.name} and his ID is {self.id} and his University is {self.university}")

e1=Employee("Rohan",6437)
e1.showdetails()
s1=Student("John",5645,"Oxford University")
s1.showdetails()