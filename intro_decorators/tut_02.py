def f1(func):
    def wrapper():
        print("start")
        func()
        print("complete")
    return wrapper


if __name__ == "__main__":
    @f1
    def f():
        print("hello")
    f()