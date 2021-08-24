"""
It's Pythons All The Way Down
Python Type & Metaclass Made Simple
"""

# A Deep dive to class

"""
- Python Types
- Python Classes
- Python Metaclasses
"""

# Python Types
"""


"""

# print(dir(int))

class Tut:
    pass

print(type(Tut))
print(type)
print(type(type))

# type.useful_value = "abcde"
Tut.useful_value = "abcde"
print(dir(Tut))

class Tut:
    def __init__(self,title):
        self.title = title

    def description(self):
        return f"tut title: {self.title}"
machine_learning_tut = Tut("machine leanring")

print(machine_learning_tut.__dict__)
print('-------')
print(machine_learning_tut.__class__.__dict__)
