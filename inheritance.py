class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f" The Name of Employee: {self.id} is {self.name}")

class Prgrammer(Employee):
    def showLanguage(self):
        print("The Default Language is Pyhthon")

        
class Student(Prgrammer):
    def showcollege(self):
        print("He is  Studying in GLA University")


e1=Employee("Elon Musk",482)
e1.showDetails()
e2=Employee("Harry",481)
e2.showDetails()

e2=Prgrammer("Harry",481)
e2.showDetails()
e2.showLanguage()

e3=Student("Prince",2242000396)
e3.showDetails()
e3.showLanguage()
e3.showcollege()

