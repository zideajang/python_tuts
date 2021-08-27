# def func():
#     msg = "hello"
#     def inner():
#         print(msg)

#     inner()

# func()

def func():
    msg = "hello"
    def inner():
        msg ="world"
    inner()
    print(msg)
func()