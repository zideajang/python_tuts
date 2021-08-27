术语**元编(metaprogramming)**程指的是一个程序有可能了解或操纵自己。Python 支持一种叫做**元类(metaclass)**的类的元编程形式。

元类是一个深奥的 OOP 概念，潜伏在几乎所有的 Python 代码背后。无论你是否意识到，你都在使用它们。在大多数情况下，你不需要意识到它。大多数 Python 程序员很少，如果有的话，不得不考虑元类。

然而，当需要的时候，Python 提供了一种并非所有面向对象语言都支持的能力：你可以在引擎盖下定义自定义元类。自定义元类的使用有些争议，正如下面这段话所暗示的那样，Tim Peters是Python大师，他撰写了《Python之禅》。

### python type
In computer science and computer programming, a data type or simple type is an attribute of data which tells the compiler or interpreter how the programmer intends to use the data

A data type **constrains** the values that an expression, such as a variable or a function, might take. This data type **defines** the operations that can be done on the data, the **meaning** of the data, and the way values of that type can be stored

#### Capabilities
```python
12 + 12
a = 12
a.__add__(3)
```

```python
dir(int) #[...,'__add__',...]
```
#### Constraints
```python
12 + "3"
```
#### Meaning
```python
type(d)
```
#### Constraints & Meaning
```python
"12" + 12
```

#### Python's Core Type
- bool
- int
- float
- complex (2 + 3j)
- bytes b"52s"
- str
- function
- class

#### Functions & Classes

```python
type(war)
type
type(type)
```

### Classes are mutable

### What is a class
- A class is a thing for constructing instances


### 类型和类(Type and Class)

在 Python 3 中，所有的类都是新式类。因此，在Python 3中，合理的做法是将一个对象的类型和它的类互换着提及。





type 是一个元类，类是 type 的实例。就像一个普通的对象是一个类的实例一样，Python 中的任何新式类，以及 Python 3 中的任何类，都是类型元类的实例。

在上面的例子中。

- x 是 Foo 类的一个实例
- Foo 是 type 元类的一个实例
- type 也是 type 元类的一个实例，所以 type 是自己的一个实例



#### Example1

在这个第一个例子中，传递给 `type() `的` <bases>` 和 `<dct>` 参数都是空的。没有指定从任何继承父类，最初也没有在命名空间字典中放置任何东西。这是最简单的类定义。



#### Example2

这里，`<bases>`是一个元组，有一个元素 Foo，指定 Bar 继承自的父类。一个属性，attr，最初被放置在命名空间字典中。



#### Example3

这一次，`<bases>`又是空的。两个对象通过 `<dct>` 参数被放入命名空间字典。第一个是一个名为 attr 的属性，第二个是一个名为 attr_val 的函数，它成为定义类的一个方法。



#### Example5

在 Python 中只有非常简单的函数可以用 lambda 定义。在下面的例子中，一个稍微复杂的函数是在外部定义的，然后通过名字 f 分配给名字空间字典中的 attr_val。





表达式Foo()创建了一个Foo类的新实例。当解释器遇到Foo()时，会发生以下情况。

Foo 的父类的 `__call__()` 方法被调用。因为 Foo 是一个标准的新式类，它的父类是 type 元类，所以 type 的 `__call__()` 方法被调用。

这个` __call__()` 方法反过来又调用了以下内容。

`__new__()`
`__init__()`
如果 Foo 没有定义` __new__()` 和 `__init__() `，默认的方法将从 Foo 的祖先那里继承过来。但是如果 Foo 定义了这些方法，它们就会覆盖那些来自祖先的方法，这就允许在实例化 Foo 时进行自定义行为。

在下面，一个叫做 new() 的自定义方法被定义并被指定为 Foo 的` __new__() `方法。