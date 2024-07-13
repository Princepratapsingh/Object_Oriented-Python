class student:
    def __init__(self, name,address):
        self.name = name
        self.address = address

e1=student("Prince","Etah")
print(e1.__dict__)#It Returns the data of self in Dictionary format
# print(help(student))#Gives information about the class Student 


x=[1,2,3]
print(dir(x))#this Gives ALl the Methods and attribute that can be applied to the x