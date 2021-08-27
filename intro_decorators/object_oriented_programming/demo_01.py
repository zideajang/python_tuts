
# basic_machine_learning_tut = ["basic machine learning",'baisc',12]
# basic_python_tut = ["basic python",'baisc',12]
# deep_learning_tut = ["basic python",'advance',6]


class Tut:
    category = "language programming"
    def __init__(self,title,lesson):
        self.title = title
        self.lesson = lesson
        
    def __str__(self):
        return f"description: title {self.title}, lesson: {self.lesson}"
   
basic_machine_learning_tut = Tut("basic machine learning",12)
print(basic_machine_learning_tut)


# print(basic_machine_learning_tut.description())

# basic_python_tut = Tut("basic python",12)

# print(f"class attributes category: {basic_machine_learning_tut.category}")
# # class attributes category: language programming
# print(f"instance attributes title :{basic_machine_learning_tut.title}")
# # instance attributes title :basic machine learning
# print(f"instance attributes lesson :{basic_machine_learning_tut.lesson}")
# # instance attributes lesson :12


# print(basic_machine_learning_tut.category)

# basic_machine_learning_tut.category = "change class attribiutes"
# print(basic_machine_learning_tut.category)

# print(basic_python_tut.category)

# class Tut:
#     pass

# print(Tut()) #<__main__.Tut object at 0x1024b1a10>

# a = Tut()
# b = Tut()
# print(a == b) #False