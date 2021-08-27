def f1(func):
    def wrapper(*args,**kwargs):
        print("start")
        func(*args,**kwargs)
        print("complete")
    return wrapper
if __name__ == "__main__":
    @f1
    def f(a):
        print(a)
    f("hello")