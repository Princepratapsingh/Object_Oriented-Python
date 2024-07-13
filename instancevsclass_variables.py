class student:
    university="GLA University"
    Noofstudents=0
    def __init__(self,name,rollno,address):
        self.name = name
        self.rollno = rollno
        self.address = address
        student.Noofstudents+=1
    def showdetails(self):
        print(f"The Student of {self.address} whose name is {self.name} studying in {self.university} and his University  rollno is {self.rollno} and total no of students in his class is {self.Noofstudents}")

s1=student("Prince Pratap Singh",2242000396,"Etah")
# student.university="Delhi University" #this will change the class varible to delhi university
s1.showdetails()
print(student.showdetails(s1))#both statements are correct 
s2=student("Nikhil Chahar",2242000347,"Agra")
s2.showdetails()
s3=student("Shyam Pathak",2242000508,"Iglas")
s3.showdetails()
s4=student("Piyush Pathak",2242000369,"Agra")
s4.showdetails()
s5=student("Shivam Pandey",2242000503,"Mathura")
s5.university="Amity University"
s5.showdetails()


