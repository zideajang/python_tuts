## Python 不再有秘密(1)—重写自定义 Python 类的操作符和内建函数的功能

> 最近在看 cpp，在 cpp 支持对自定义类的操作符进行重载，python 是我们自己了解语言中比较接近 cpp 的语言

例如我们了解用于数值型的操作符 + 和 * 用于字符串类型会有不同的行为。
```python
print(2 + 3) #5
print('Hello' + ' ' + "machine leanring") #Hello machine leanring
print('python'*3) # pythonpythonpython
```

你可能已经想知道为什么同一个内建运算符或函数对不同类的对象显示出不同的行为。这被分别称为操作符重载或函数重载。这篇文章将帮助你理解这种机制，这样你就可以在你自己的Python类中做同样的事情，使你的对象更加Pythonic。

### 你将了解到
- 在 Python 中处理运算符和内建的 API
- len()和其他内建函数背后的 "秘密"
- 如何使你的类能够使用运算符
- 如何使你的类与 Python 的内建函数兼容



### Python 数据模型

用户喜欢一个课程，可能当时没有时间或者看过之后还想温故而知新，可以将课程进行收藏，也就是每一个用户都有一个收藏课程列表。

在这种情况下，想要获得用户收藏列表的长度。初学 Python 的人可能会决定在他们的类中实现一个叫做 get_tuts_len() 的方法来完成这个任务。也可以以这样的方式配置内建的 len() ，当给定我们的对象时，复写内建 len 方法返回收藏列表的长度。

在另一种情况下，我们可能想往收藏夹添加一个课程。同样，刚接触 Python 的人会想到实现一个叫做 `append_to_cart() `方法来实现往收藏列表中追加课程，接收一个课程对象并将其添加到收藏列表中。同样也可以 + 操作符方式来实现把一个新的课程追加到收藏夹中。

在 Python 中所提供的特殊的方法的命名都是在方法名字前有两个下划线开始，方法名后面两个下划线结束，例如`__len()__`

基本上，每个内建函数或运算符都有一个与之对应的特殊方法。例如，有`__len__()` 对应于len()，和 `__add__()`对应于 + 运算符。

在默认情况下，大多数的内建函数和运算符不会支持对自定义类进行操作。要想要你的类可以调用这些内建函数和运算符，则需要在类定义中添加相应的特殊方法并给予实现。

这正是数据模型 (Data Model) 帮助你完成的工作。列出了所有可用的特殊方法，并提供了重载内建函数和运算符的方法，这样你就可以在自己的对象上使用这些方法。



### 内联的操作符

#### 内建操作符 len() 和 []

Python 中的每个类都为内建函数和方法定义了自己的行为。当你把某个类的实例传递给一个内建函数或在实例上使用一个操作符时，实际上相当于用相关参数调用一个特殊方法。

如果有一个内建函数，func()，并且该函数对应的特殊方法是` __func__()`，Python 将对该函数的调用解释为 `obj.__func__()`，其中 obj 是对象。在操作符的情况下，如果你有一个操作符 opr，并且它对应的特殊方法是` __opr__()`，Python 将类似` obj1 <opr> obj2 `的解释为 `obj1.__opr__(obj2)`。

所以，当你在一个对象上调用 len() 时，Python 将调用处理为` obj.__len__()`。当你在一个可迭代的对象上使用 `[] `操作符来获取索引处的值时，Python 以 `itr.__getitem__(index)` 的方式处理，其中` itr` 是可迭代的对象，index 是你想要获取的索引。

因此，当你在自己的类中定义这些特殊方法时，你覆盖了与之相关的函数或操作符的行为，因为在幕后，Python 正在调用你的方法。让我们对此有一个更好的理解。

```python
a = 'machine learning'
b = ['machine','learning']

print(len(a))#16
print(a.__len__())#16

print(b[0])#machine
print(b.__getitem__(0))#machine
```



### 重写内建方法

数据模型中定义的许多特殊方法可以用来改变函数的行为，如 `len`、`abs`、`hash`、`divmod` 等等。要做到这一点，只需要在你的类中定义相应的特殊方法。让我们来看看几个例子。
#### 重写内建 len() 方法

想要将自定义类 Favority 也得到内建函数`len()`的支持，需要在 Favority 类中实现一下 `__len__()`特殊方法。这样把 Favority 实例的对象传递给 `len()` 时，就会调用 Favority 类的` __len__()` 返回`self.favority` 的长度。

```python
class Favority:
    def __init__(self, favority, user):
        self.favority = list(favority)
        self.user = user
    
    def __len__(self):
        return len(self.favority)


favority = Favority(['machine leanring','deep learning','reinforcement leanring'],'mike')
print(len(favority))#3
```
如果在 Favority 类没有实现 `__len__` 然后再将 Favority 类的实例传入到 `len()` 就会抛出 `TypeError` 错误。

```python
class Favority:
    def __init__(self, favority, user):
        self.favority = list(favority)
        self.user = user
```

```python
    print(len(favority))#3
TypeError: object of type 'Favority' has no len()
```

```python
class Favority:
    def __init__(self, favority, user):
        self.favority = list(favority)
        self.user = user
    
    def __len__(self):
        return float(len(self.favority))
```
如果定义内建方法`__len__()` 返回值类型是浮点型而非要求整型，也会抛出如下异常。

```
TypeError: 'float' object cannot be interpreted as an integer
```

#### 重写内建函数 abs()

为自定义向量类(Vector) 定义一个特殊函数 `__abs__` 以对应于内建函数 `abs()`。在向量类的实例作为参数输入到内建函数`abs` 返回一个向量的长度

```python
class Vector:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

vec = Vector(2,3)
print(abs(vec)) #3.6
```

#### 重写内建函数 str()
`str()`内建函数可以将一个类的实例转换为一个`str`对象，通过打印输出可以使用者了解到这个类，便于阅读和调试，可以通过在自定义类中实现 `__str__()` 方法，当自定义类的对象传入给内建` str() `函数时，就会执行自定义类的`__str__()` 返回描述对象的字符串，同样在调用调用` print() `时也会调用该方法。


```python
class Vector:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f"x component:{self.x},y component:{self.y}"
vec = Vector(2,3)
# print(abs(vec)) #3.6
print(str(vec)) #x component:2,y component:3
print(vec)#x component:2,y component:3
```

#### 重写内建函数 repr()
str 对应类的 `__str__(self)`,repr 对应类的` __repr__(self)`,repr 一般用于进行 report，即对当前实例进行一个简报，内容应当是对类型和实例结构的反射信息，str 一般用于执行 tostring， 即强制转换为字符串，是类型转换主要手段

`repr()` 内置函数用于获得一个对象的可解析字符串表示。如果一个对象是可解析的，这意味着当` repr` 与` eval()` 等函数一起使用时，Python 应该能够从这个表示中重新创建这个对象。为了定义` repr()` 的行为，你可以使用 `__repr__() `特殊方法。

这也是 Python 用来在 REPL 会话中显示对象的方法。如果没有定义 `__repr__()` 方法，你会得到类似 `<__main__.Vector object at 0x...>` 的东西，试图在 REPL 会话中查看该对象。让我们看看它在Vector类中的作用。

```python
a = 3
print(repr(a))#3

b = 'machine leanring'
print(repr(b)) #'machine leanring'

class Developer:
    def __init__(self,name):
        self.name = name
    
    def __repr__(self):
        return f"my name is {self.name} and a developer"

mike = Developer("mike")
print(repr(mike)) #my name is mike and a developer
```

#### 重写内建函数 bool()



### 重写操作符功能

#### 重写加法操作符 

```python
class Favority:
    def __init__(self, favority, user):
        self.favority = list(favority)
        self.user = user
    
    def __len__(self):
        return len(self.favority)

    def __add__(self,tut):
        new_favority = self.favority.copy()
        new_favority.append(tut)
        return Favority(new_favority,self.user)    

favority = Favority(['machine leanring','deep learning','reinforcement leanring'],'mike')
favority = favority + 'pytroch tut'
favority = favority + 'tensorflow tut'
# ['machine leanring', 'deep learning', 'reinforcement leanring', 'pytroch tut', 'tensorflow tut']
print(favority.favority)

```



#### 重写快捷方式 +=  操作符


#### 重写[] 操作符

`[]` 操作符也被称为索引操作符，通过这个操作符可以序列中获取索引处的值，在字典中获取该键对应的值，支持 slice 操作从序列中获取一部分数据。可以使用` __getitem__()`特殊方法让自定义类支持该操作符。对收藏夹类进行适当修改，以便我们可以直接从收藏夹获取得到一个课程。

```python
class Favority:
    def __init__(self, favority, user):
        self.favority = list(favority)
        self.user = user
    
    def __len__(self):
        return len(self.favority)

    def __getitem__(self,key):
        return self.favority[key]

favority = Favority(['machine leanring','deep learning','reinforcement leanring'],'mike')
print(favority[0]) #machine leanring
print(favority[-1])#reinforcement leanring
```

你会注意到，在上面，`__getitem__()`的参数名称不是 index，而是 key。这是因为参数主要有三种形式：一个整数值，在这种情况下，可以是一个索引，或者是一个字典的键，一个字符串值，在这种情况下，它是一个字典的键；一个切分对象，在这种情况下，它将切分类所使用的序列。虽然还有其他的可能性，但这些是最常遇到的。

由于我们的内部数据结构是一个列表，我们可以使用 [] 操作符来切分这个列表，因为在这种情况下，键值参数将是一个切分对象。这是在你的类中有一个` __getitem__()` 定义的最大优势之一。只要你使用的是支持切分的数据结构（列表、图元、字符串等等），你就可以配置你的对象来直接切分该结构。







