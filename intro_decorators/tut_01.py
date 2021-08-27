def f1():
    print("hello")

def f(func):
    func()

if __name__ == "__main__":
    f(f1)