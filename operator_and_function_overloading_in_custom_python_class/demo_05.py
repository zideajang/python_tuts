
a = 3
print(repr(a))#3

b = 'machine leanring'
print(repr(b)) #'machine leanring'

class Developer:
    def __init__(self,name):
        self.name = name
    
    def __repr__(self):
        return f"my name is {self.name} and a developer"

mike = Developer("mike")
print(repr(mike)) #my name is mike and a developer
