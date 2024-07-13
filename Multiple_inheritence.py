class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def show(self):
         return f"The Name of employee is {self.name} and his id is {self.id}"

class Programmer:
    def __init__(self,lang):
        self.lang = lang
    def show(self):
        return f"The Language is {self.lang}"


class Student(Employee, Programmer):
    def __init__(self,name,id,lang,university):
        Employee.__init__(self,name,id)#Multiple super not callable 
        Programmer.__init__(self,lang)
        self.university = university
    def show(self):
        employee_info = super().show()  # Call Employee's show method
        return f"{employee_info} and his favorite language is {self.lang} and studying in {self.university}"

s=Student("Prince",7548,"Python","GLA University")

print(s.show())
    