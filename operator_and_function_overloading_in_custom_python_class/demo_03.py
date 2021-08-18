class Vector:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f"x component:{self.x},y component:{self.y}"
vec = Vector(2,3)
# print(abs(vec)) #3.6
print(str(vec)) #x component:2,y component:3
print(vec)#x component:2,y component:3
    