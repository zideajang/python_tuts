print(type(42))#<class 'int'>
print(type(42.0))
print(type('foo'))

a = 42
a = float(a)
a = str(float(a))
a = list(str(float(a)))
print(a)