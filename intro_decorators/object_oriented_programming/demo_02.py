
# tuts = ["basic_machine_learning_tut","basic_python_tut","deep_learning_tut"]
# print(tuts)#['basic_machine_learning_tut', 'basic_python_tut', 'deep_learning_tut']

class Tut:
    category = "language programming"
    def __init__(self,title,lesson):
        self.title = title
        self.lesson = lesson
        
    def __str__(self):
        return f"description: title {self.title}, lesson: {self.lesson}"
    def summary(self,intro):
        return ""
   
class MachineLearningTut(Tut):
    pass
class LanguageProgrammingTut(Tut):
    pass