def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

time3 = make_multiplier_of(3)
time5 = make_multiplier_of(5)
print(time3(2))

print(make_multiplier_of.__closure__) #None
print(time3.__closure__[0].cell_contents) #3
print(time5.__closure__[0].cell_contents) #5