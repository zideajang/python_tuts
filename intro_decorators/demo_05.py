
def before_and_after(func):
    def wrapper(text):
        print("BEFORE")
        func(text)
        print("AFTER")

    return wrapper

@before_and_after
def greet(text):
    print(f"hi {text}")

greet("decorators")

# def before_and_after(func):
#     def wrapper()


# def params(*args,**kwargs):
#     print(f"{args}")
#     print(f"{kwargs}")

# params(1,2,name="decorators tut")



def before_and_after(func):
    def wrapper(*args,**kwargs):
        print("BEFORE")
        value = func(*args,**kwargs)
        print("AFTER")
        return value

    return wrapper

# def params(*args, **kwargs):
#     print(args)
#     print(kwargs)

# params(1,2,name="decorators")

@before_and_after
def adder(num_1,num_2):
    return num_1 + num_2

# 介绍 Python 中的闭包以及闭包应用，例如偏函数、currying 和修饰器
res = adder(2,3)
print(res)

# print(adder) #<function before_and_after.<locals>.wrapper at 0x1029d6a70>

# def before_and_after(func):
#     def wrapper(*args,**kwargs):
#         print("BEFORE")
#         value = func(*args,**kwargs)
#         print("AFTER")
#         return value

#     return wrapper

# @before_and_after
# def adder(num_1,num_2):
#     return num_1 + num_2


# print(adder(2,3))