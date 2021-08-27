class Employee:
    def __init__(self,name,age):
        print("employee init()")
        self.name = name
        self.age = age

    def intro(self):
        return f"my name is {self.name} and {self.age} year old"
    
    def salary(self):
        return "salaray"

class Developer:
    def __init__(self,lang):
        print("developer init()")
        self.lang = lang

    def intro(self):
        return f"I'm a developer and can code {self.lang}"

class ADeveloperEmployee(Developer,Employee):
    pass

mike = ADeveloperEmployee("python") #developer init()
print(mike.intro())
print(mike.salary())

# print(isinstance(mike,Employee)) #True
# print(isinstance(mike,Developer)) #True

print(ADeveloperEmployee.__mro__)
