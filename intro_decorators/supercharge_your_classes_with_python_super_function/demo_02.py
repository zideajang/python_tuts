class Tut:
    def __init__(self,title,lesson):
        self.title = title
        self.lesson = lesson
    
    def descrition(self):
        return f"title: {self.title} , lesson: {self.lesson}"

# 
class Video:
    def __init__(self,title,lesson):
        self.title = title
        self.lesson = lesson

    def descrition(self):
        return f"play: {self.title}  video"

# 
class VideoTut(Tut,Video):
    def __init__(self,title,lesson):
        self.title = title
        self.lesson = lesson
    
    def descrition(self):
        descrition = super.descript()
        # print(descrition)
        return f"title: {self.title} , lesson: {self.lesson} {descrition}"

a_video_tut = Video("videotut",12)
print('-'*50)
print(a_video_tut.descrition())