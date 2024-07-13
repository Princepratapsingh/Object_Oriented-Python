class employee:
    def __init__(self):
        self.name="Anuj" #Publically acessible Modifiers
        self.__name="Anuj" #Private acessible Modifiers Name Mangling Required
        self._name="Anuj" #Protected acessible Modifiers
a=employee()
# print(a.__name)#cannot be accessed directly
print(a._name)#can be accessed directly
print(a._employee__name)#can be accessed indirectly
print(dir(a))#Types of Methods that can be applied 
