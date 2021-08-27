# printer = print()
# print(printer)



def prefix_factory(prefix):
    def prefix_print(text):
        print(f"{prefix}: {text}")
    return prefix_print

debug = prefix_factory("DEBUG")
# print(debug)

# debug("decorators")


def reverse_factory(func):
    def reverse_caller(text):
        func(text[::-1]) # greet text(decorators)r
    return reverse_caller

# reverse_print = reverse_factory(print)
# reverse_print("decorators")


@reverse_factory
def greet(name):
    print(f"hi {name}")

# greet = reverse_factory(greet)
greet("decorators")

# greet = reverse_factory(greet)
# greet("decorators")