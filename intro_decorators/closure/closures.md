

将学习 Python 闭包，在 python 如何定义一个闭包，以及如何使用闭包。

### 嵌套函数中的非局部变量
在讨论什么是闭包之前，有必要先了解什么是嵌套函数和非局部变量。在一个函数内部定义函数称为嵌套函数。嵌套函数是可以访问其所在函数内部的变量的，如下

```python
def func():
    msg = "hello"
    def inner():
        print(msg)

    inner()

func()
```

.

在 Python 中，这些非局部变量 (`msg = "hello"`) 默认是只读的，如果想要在嵌套函数里` inner()`  修改外部  `msg`，就需要显示通过关键字  `nonlocal` 明确地将其声明为非局部变量 ，然后才能对其进行修改。

```python
def func():
    msg = "hello"
    def inner():
        msg ="world"
    inner()
    print(msg) # hello
func()
```

如果想要修改作用域在 func 范围内的 msg 变量，需要在其前面添加 nonlocal

```python
def func():
    msg = "hello"
    def inner():
        nonlocal msg
        msg ="world"
    inner()
    print(msg)# print world
func()
```



### 定义闭包

在上面的例子中，如果函数 `print_msg()` 的最后一行返回 `printer` 函数而不是调用这个函数，会发生什么？这意味着该函数被定义如下。

```python
def print_msg(msg):

    def printer():
        print(msg)

    return printer  # returns the nested function


# Output: Hello
another = print_msg("Hello")
another()
```

调用  `print_msg() `函数时传入参数为字符串 "Hello "，返回的函数赋值到变量 another 上。当调用 `another()` 时，尽管已经完成了 `print_msg()` 函数的执行，但是 msg 变量值还是被保留了。这种将一些数据 (在本例中为 "Hello") 由内部函数调用该变量，当包裹函数执行结束后，该变量还得以保留，技术上在 Python 中被称**闭包**。

```python
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
```

#### 我们什么时候有闭包？
从上面的例子中可以看出，当一个嵌套的函数在其包围的范围内引用一个值时，我们在 Python 中就有一个闭包。

在 Python 中创建闭包必须满足的条件被总结为以下几点。

- 存在嵌套函数 
- 通常在嵌套函数引用定义在外部函数中的变量
- 外部函数需要将嵌套函数返回

#### 何时使用闭合器？
那么，闭包有什么用呢？接下来就看一看闭包的一些作用。闭包可以避免使用全局变量，并提供某种形式的变量私有，也就是提供一种面向对象的解决方案。当一个类中需要实现的方法很少(大多数情况下是一个方法)时，闭包可以提供另外一种实现封装方式、更优雅的解决方案。但如果属性和方法的数量变多时，最好还是实现一个类。

```python
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))

```



Python装饰器实现方式也会也大量使用闭包。最后要指出的是，封闭函数中被封闭的值是可以被发现的。



```python
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


print(make_multiplier_of.__closure__) #None
```



所有的函数对象都有一个 `__closure__` 属性，如果是一个闭包函数，则返回一个单元格对象的元组。参照上面的例子，我们知道`times3`和`times5`是闭合函数。



```python
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
```

