# a_tut = "machine leanring tut"
# lang_tuts = ["js","java","python","cpp","golang"]

# print(a_tut.__len__())
# print(lang_tuts.__getitem__(0))

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    pass

# class Square(Rectangle):
#     def __init__(self, length):
#         super().__init__(length, length)

    