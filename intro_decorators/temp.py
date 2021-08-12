# python 
# print("hello world")
# trick 很多，很灵活，有一定深度
# 如何 efficiently 写 python


# 第一个装饰器
# print("hello decorators")
# proxy_printer = print
# proxy_printer("hello decorators")

def reverse(text):
    print(text[::-1])

def greet(name,printer=print):
    printer(f"hi {name}")

def add(num1,num2):
    return num1 + num2

def add_factory(num1):
    def add(num2):
        return num1 + num2

    return add

add2 = add_factory(2)
print(add2(3))

greet("decorators",printer=reverse)