
# def func():
#     hello = "hello"
#     def inner_func():
#         return hello
#     return inner_func
    
# get_hello = func()
# print(get_hello())

# my_printer = print
# my_printer("hello closure")

# partial function
def add(num_1,num_2):
    return num_1 + num_2

def add2(num):
    return add(2,num)


# production 50 * 50 * x

# def volumn(h):
#     def volumn_h(w):
#         def 

def curried_add(num_1):
    def wrapper(num_2):
        return add(num_1,num_2)
    return wrapper

# res = add2(3)
# print(res)

add2 = curried_add(2)

res_1 = add2(5)
res = add2(3)
print(res_1)

