# proxy_print = print
# proxy_print("hi decoration")

def greet(name,printer=print):
    printer(f"hi {name}")

# print(greet("machine learning"))
def reverse(text):
    print(text[::-1])

greet("hi decorations",printer=reverse)