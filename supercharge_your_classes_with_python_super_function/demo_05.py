class Developer:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self,lang):
        return f"my name is {self.name} can write {lang}"

    def __str__(self):
        return f"my name is {self.name} and {self.age} years old"

class PythonDeveloper(Developer):
    
    def intro(self,lang='python'):
        return super().intro(lang)

class JavaDeveloper(Developer):
    pass

class JavaScriptDeveloper(Developer):
    pass

mike = PythonDeveloper("mike",28)
# tony = JavaDeveloper("tony",32)
# kerry = JavaScriptDeveloper("kerry",26)

# print(isinstance(mike,Developer)) #True
# print(type(mike)) #<class '__main__.PythonDeveloper'>

# print(mike) #my name is mike and 28 years old
print(mike.intro()) #my name is mike can write python

# print(isinstance(mike,JavaScriptDeveloper)) #False