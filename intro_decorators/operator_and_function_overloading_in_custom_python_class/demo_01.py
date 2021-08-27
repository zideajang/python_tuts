
# print(2 + 3) #5
# print('Hello' + ' ' + "machine leanring") #Hello machine leanring
# print('python'*3) # pythonpythonpython

# a = 'machine learning'
# b = ['machine','learning']

# print(len(a))#16
# print(a.__len__())#16

# print(b[0])#machine
# print(b.__getitem__(0))#machine

# python Data model

class Tuts:
    def __init__(self,tuts):
        self.tuts = tuts

    def __len__(self):
        return len(self.tuts)

    def __str__(self):
        return str(self.tuts)

    def __add__(self,tut):
        new_tuts = self.tuts.copy()
        new_tuts.append(tut)
        return Tuts(new_tuts)

    def __getitem__(self,key):
        return self.tuts[key]
    
    def get_tut_by_index(self,key):
        return self.tuts[key]

    def is_empty(self):
        if len(self.tuts) > 0:
            return True
        return False
        
tut = Tuts(["basic python","web programming"])

# print(len(tut))
# print(str(tut)) #<__main__.Tuts object at 0x1048c6250>
# print(tut[0])#basic python
# tut + "machine leanring" #['basic python', 'web programming']
print(tut)
