class Tut:

    category = "language programming"

    def __init__(self,title,lesson_num):
        self.title = title
        self.lesson_num = lesson_num
    
    def intro(self,lang):
        return f"lang:{lang},title: {self.title} ,lesson num:{self.lesson_num} "

# reusable, struction extend
# type
class PythonTut(Tut):
    def methodOfChild(self):
        return "method of child class"

    def intro(self,lang="python"):
        return super().intro(lang)
    
class JavascriptTut(Tut):
    pass
        
