class student:
    name="Prince Pratap Singh" #Default Values
    Occupation="Student" 
    UniversityRollno=2242000396
    def info(self):
        print(f"{self.name} is a {self.Occupation}")
a=student()
b=student()
c=student()
d=student()
e=student()
b.name="Nikhil"
b.Occupation="Fullstack developer"
c.name="Shyam"
c.Occupation="Software Engineer"
d.name="Piyush"
d.Occupation="Project Manager"
e.name="Shivam"
e.Occupation="Python developer"
a.Occupation="Web Developer"

a.info()
b.info()
c.info()
d.info()
e.info()
