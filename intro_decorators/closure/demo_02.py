def print_msg(msg):

    def printer():
        print(msg)

    return printer  # returns the nested function


# Output: Hello
another = print_msg("Hello")
another()

del print_msg
another() # Hello
# print_msg("Hello")