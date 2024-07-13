class student:
    # name ="Prince Pratap Singh" #Default Values
    # Occupation="Student" 
    # UniversityRollno=2242000396
    # we can use contructors instead of using the above ,method 
    def __init__(self,name,occ):
        print("Jai shree Ram") #default constructor
        self.name=name#parammeterized constructor
        self.occ=occ
        
    def info(self):
        print(f"{self.name} is a {self.occ}")
a=student("Prince Pratap Singh","Front-end Developer")
b=student("Nikhil Chahar", "Fullstack Developer")
c=student("Shyam  Pathak", "Software Developer")
d=student("Piyush Pathak", "Project Manager")
e=student("Shivam Pandey","Python Developer")
a.info()
b.info()
c.info()
d.info()
e.info()
# f=student()#This Gives the error
# f=student(1,2,3)#this also gives the error because i pass  four arguments instead of three,in this case self is automatically called when we write only f=student()