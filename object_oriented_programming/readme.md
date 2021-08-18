

> 其实许多知识点，我们看似已经熟悉还不能再熟悉，而且有些代码已经成为习惯，因为我们对他们太熟悉了，而忘记问一句为什么会这样写，所以适当抽出时间对一些过往的或者熟悉知识进行整理，可能会有意想不到的收获

### Python 语言对面向对象的支持

当初 OOP 这种设计模式有多火，就连销售经理在跟客户谈时候，是不是都会用一两次这个术语—面向对象。不过这两年其势头有点被 FP(函数式编程)盖过，不过大多数情况下我还是会选择面向对象方式进行建模和组织代码，那么什么是面向对象编程



#### 什么是面向对象编程

面向对象的编程是一种**编程范式**，提供了一种结构化程序的方法，将属性和行为绑定到单个对象中。换句话说，面向对象编程是一种对具体的、现实世界的事物进行建模的方法，如汽车，以及事物之间的关系，如公司和雇员、学生和教师，等等。



面向对象的编程是一种**编程范式**，提供了一种结构化程序的方法，将属性和行为绑定到单个对象中。也就是定义数据结构，数据结构反应一个事物，例如商品是集合名称，是抽象的对商品描述，具有一般性。而具体一个商品是一个实例，具有商品的名称、规格和售价等属性。还有电子邮件，其属性包括收件人列表、主题和正文，以及添加附件和发送等行为。


> 可能大家对 OOP 认识会有点偏差，就是 OOP 不仅是对现实事物进行建模的方法，设计程序时将真实事物对应到面向对象一个类，面向对象中类是一种数据结构，面向对象 OOP 目标是有效合理地去组织代码。是我们如何实现多人开发有效组织代码的解决方案，这是到今天为止我对面向对象一点认识。

#### 什么是过程式编程

OOP 将现实世界的实体建模为软件对象，这些对象有一些与之相关的数据以及行为以对象形式组织在一起。另一种常见的编程范式是过程化编程，像根据食谱来烹饪一个美味的菜肴一样来设计程序，按照做事流程来组织代码完成一项任务。

关键的启示是，对象是  Python 中面向对象编程的中心，不仅像程序式编程那样代表数据，而且在程序的整体结构中也是如此。



### 在 python 定义类

基本数据结构，如 `numbers`、`string` 和 `list` 设计这些基本类型用来表示简单的信息，例如一套课程的，水果或最喜欢的颜色，这样用基本数据类型是无法表示，我们需要更复杂数据类型来描述这些事物。

例如，需要维护一个发布的课程列表。需要存储每套课程的的一些基本信息，如课程标题、难度级别、课程数。

```python
basic_machine_learning_tut = ["basic machine learning",'baisc',12]
basic_python_tut = ["basic python",'baisc',12]
deep_learning_tut = ["basic python",'advance',6]
```

这种表示方式存在着一些问题

- 难于管理和维护，当使用引用 `basic_machine_learning_tut[0]` 我们需要熟悉在列表索引为 0 值对应是课程哪一个属性，是课程名称还是课程数
- 难于维护，一旦某一条记录有数据遗漏就会发生数据错位，随着带来获取数据不正确。

用类(class)维护数据好处，就是可读性和易于维护

#### 类和实例

类是用来创建用户定义的数据结构。在类中定义的函数称为方法，方法用于如何基于类来创建一个对象，可以用于操作数据，例如定义如何获取数据，如何更新数据。接下来围绕课程这个类，来分享如何定义一个类以及使用一个类。类是抽象对事物描述，是对一类事物的抽象，例如学生、职员和公司，我们根据业务对这些事物进行抽象，给出一个描述，有点类似生成零件设计图纸，其中并不包含任何实际数据，当然也会包含一些对象间共享方法和数据。

有了图纸，我们就可以根据图纸来定义一个实例(对象)，对象相对于类是一个具体的数据结构。

#### 在 Python 如何定义一个类

```python
class Tut:
    pass
```

在 python 中定义类，使用 class 关键字后面给类名称，类作为一个集合通常是首字母大写具有实际意义的名称，可以用驼峰式命名来为类进行命名， pass 通常被用作占位符，避免在方法或函数体中没有实现而抛出一个错误。

所有课程对象必须具备的一些属性可以放一个叫做`.__init__()` 的方法中定义，可以将方法理解类构造函数。每次创建一个新的课程对象时，在初始化`.__init__()`通过分配对象的属性值来初始化对象的属性。也就是说，`.__init__() `初始化了该类的实例。`__init__()`的第一个参数总是 `self` 然后随后是其他参数。

```python
class Tut:
    def __init__(self,title,lesson):
        self.title = title
        self.lesson = lesson
        
```



在 `__init__()`中定义属性属于实例属性，每一个实例属性的这些属性因实例不同而不同。如果类属性，我们需要`__init()__` 以外进行定义，在类级别上定义属性是所有该类所有对象所共享。

```python
class Tut:
    category = "language programming"
    def __init__(self,title,lesson):
        self.title = title
        self.lesson = lesson
```



`category = "language programming"` 在 class 定义语句下开始定义类级别属性，类级别属性必须给初值，`category` 属性有该类实例化的对象所共享。

```python
class Tut:
    category = "language programming"
    def __init__(self,title,lesson):
        self.title = title
        self.lesson = lesson
        

basic_machine_learning_tut = Tut("basic machine learning",12)
print(basic_machine_learning_tut.category)
```

在实例上是可以修改类属性，不过实例上修改类属性后并不会影响到该类的其他对象的该属性值。

```python
class Tut:
    category = "language programming"
    def __init__(self,title,lesson):
        self.title = title
        self.lesson = lesson
        

basic_machine_learning_tut = Tut("basic machine learning",12)
print(basic_machine_learning_tut.category)#language programming

basic_machine_learning_tut.category = "change class attribiutes"
print(basic_machine_learning_tut.category)#change class attribiutes

basic_python_tut = Tut("basic python",12)
print(basic_python_tut.category)#language programming
```



### 在 python 如何化一个实例



```python
class Tut:
    pass

print(Tut()) #<__main__.Tut object at 0x1024b1a10>
```

这里实例化一个类的对象，像调用方法一样，用类名加上一对圆括号`Tut()`就会实现了实例化了一个 Tut 的实例，创建有一个新的 Tut 对象，位于`0x1024b1a10`，数字串是一个内存地址，表明课程对象在你的计算机内存中的存储位置。



```python
a = Tut()
b = Tut()
print(a == b) #False
```



每实例化一个 Tut 对象，系统就会为该对象分配一个新的内存地址用于存放这个对象。在这段代码中，你创建了两个新的课程对象，并把赋值给给了变量 a 和 b。用 == 运算符判断 a 和 b 是否相等时，结果是 `False`。尽管 a和 b 都是课程类的实例，因为在内存地址不同，所以代表两个不同的对象。



#### 类和实例的属性

通过下面代码，大家可以了解到如何在类如何定义类和对象属性以及任何调用这些属性，因为代码比较易懂，就不做过多介绍

```python
class Tut:
    category = "language programming"
    def __init__(self,title,lesson):
        self.title = title
        self.lesson = lesson
        

basic_machine_learning_tut = Tut("basic machine learning",12)
basic_python_tut = Tut("basic python",12)

print(f"class attributes category: {basic_machine_learning_tut.category}")
# class attributes category: language programming
print(f"instance attributes title :{basic_machine_learning_tut.title}")
# instance attributes title :basic machine learning
print(f"instance attributes lesson :{basic_machine_learning_tut.lesson}")
# instance attributes lesson :12
```

在实例化时，除了 self 参数是由系统完成赋值的，其他两个参数`title·`和`lesson`需要赋值，



```python
class Tut:
    category = "language programming"
    def __init__(title,lesson):
        # self.title = title
        # self.lesson = lesson
        title.lesson = lesson
        
a = Tut(12)
print(a.lesson)
```

注意这里`self` 不能省略，这里第一个参数名称可以不使用 self 而自己给出一个新的名称，如下

```python
class Tut:
    category = "language programming"
    def __init__(title,lesson,others):
        # self.title = title
        # self.lesson = lesson
        title.lesson = lesson
        title.others = others
        
a = Tut(12,"others")
print(a.lesson) #12
print(a.others) #others
```

#### 实例的方法

实例方法是在一个类中定义的函数，只能从该类的实例中调用该函数。和` .__init__()` 一样，实例方法的第一个参数总是 `self`。

```python
class Tut:
    category = "language programming"
    def __init__(self,title,lesson):
        self.title = title
        self.lesson = lesson
        
    def description(self):
        return f"description: title {self.title}, lesson: {self.lesson}"


basic_machine_learning_tut = Tut("basic machine learning",12)
print(basic_machine_learning_tut.description())
```



在上面的 Tut 类中，`.description()`返回一个包含课程实例信息的字符串。当然在编写自己的类时，定义一个方法来返回一个包含该类实例的有用信息的字符串并没有什么不妥之处。然而这么做`.description()`并不是最符合 Pythonic 的方式。

```python
print(basic_machine_learning_tut) #<__main__.Tut object at 0x10186b250>
```

当我们输出实例化的对象`basic_machine_learning_tut` 返回的信息是对象位置内存地址位置的信息，我们再来看一看输出 `list` 对象，如下

```python
tuts = ["basic_machine_learning_tut","basic_python_tut","deep_learning_tut"]
print(tuts)#['basic_machine_learning_tut', 'basic_python_tut', 'deep_learning_tut']
```

 你可以通过定义一个名为` .__str__() `的特殊实例方法来改变打印对象的内容。

```python
class Tut:
    category = "language programming"
    def __init__(self,title,lesson):
        self.title = title
        self.lesson = lesson
        
    def __str__(self):
        return f"description: title {self.title}, lesson: {self.lesson}"
   
basic_machine_learning_tut = Tut("basic machine learning",12)
print(basic_machine_learning_tut)
```



像 `.__init__() `和 `.__str__()` 这样的方法被称为 dunder/magic 方法，通常这些方法都是以双下划线开始和结束。有许多 dunder/magic 方法，可以用来定制 Python 中的类,但理解 dunder/magic 方法是掌握 Python 中面向对象编程的一个重要部分。

### 在 Python 实现类的继承

面向对象的编程的三大特征—封装、继承和多态，其中继承是一个类接受另一个类的属性和方法的**过程**。继承同时具有两种含义

- 继承基类的方法，并做出自己的改变和/或扩展从而主要为了解决了代码重用问题
- **声明**某个子类**兼容**于某基类（或者说，接口上完全**兼容**于基类），外部调用者可无需关注其差别

#### 父类和子类

```python
class Developer:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self,lang):
        return f"my name is {self.name} can write {lang}"

    def __str__(self):
        return f"my name is {self.name} and {self.age} years old"
```



然后我们定义一下 `Developer` 的子类，在 python 里要实现继承某一个类十分简单，只需要在类名称后面加一个圆括号中填入其父类名称即可，具体操作如下



```python
class PythonDeveloper(Developer):
    pass

class JavaDeveloper(Developer):
    pass

class JavaScriptDeveloper(Developer):
    pass
```

即使我们没有对类进行任何定义，因为继承了类 Developer 类，所以实例化一个 `PythonDeveloper` 的对象 `mike`就拥有了其父类的属性和方法。

```python
mike = PythonDeveloper("mike",28)
print(mike) #my name is mike and 28 years old
print(mike.intro("python")) #my name is mike can write python
```

接下来分别实例化了上面定义的继承于父类 Developer 的 3 个子类

```python
mike = PythonDeveloper("mike",28)
tony = JavaDeveloper("tony",32)
kerry = JavaScriptDeveloper("kerry",26)
```

我们查看一下实例化 `PythonDeveloper` 的对象 `mike` 的类型为 `PythonDeveloper` 并且

```python
print(isinstance(mike,Developer)) #True
print(type(mike)) #<class '__main__.PythonDeveloper'>
```



```python
print(isinstance(mike,JavaScriptDeveloper)) #False
```



#### 扩展父类的功能

擅长不同语言程序员具有不同`intro`方法，我们想要在定义类时候就给出按语言对程序员进行类别划分的成员语言一个默认值，例如 `PythonDeveloper` 的`intro`方法语言(lang)默认值为 `python`。这样这只是简单地演示如何扩展父类的方法能力，然后再这个与父类同名的方法`intro` 调用一下父类的`intro`方法

```python
class PythonDeveloper(Developer):
    def intro(self,lang='python'):
        return super().intro(lang)
```

很多情况我们需要完全重写父类的方法，这个例子我们还需要保留父类的 `intro` 以便父类的该方法发生改变后会影响到 `PythonDeveloper` 子类。所以在子类 `PythonDeveloper` 的与父类同名方法`intro`又调用了父类 `Developer` 的 `intro` 方法。

```python
print(mike.intro()) #my name is mike can write python
```



>  关于类的继承，需要记住的一点是，对父类的改变会自动传播到其子类。除非子类复写该属性或方法



### 在 Python 中的多继承

Python 还支持多继承，在这种情况下，一个子类可以继承于多个不一定相互继承的超类。我们现在看一看一个子类是否可以进行多继承，有关多继承在一些面向对象语言中是不支持的。下面例子看起好像有点不合理，仅是为了演示，定义了两个类分别是 Employee 和 Developer。

#### 实现多继承

```python
class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        return f"my name is {self.name} and {self.age} year old"
    
    def salary(self):
        return "salaray"

class Developer:
    def __init__(self,lang):
        self.lang = lang

    def intro(self):
        return f"I'm a developer and can code {self.lang}"
```

Empoyee 和 Developer 构造函数分别接受两个参数和一个参数，同时拥有 intro，多继承在 python 中也十分简单，就是定类时在类名的圆括号中分别放入 Employee 和 Developer，注意一些这两类时有顺序的。

```python
class ADeveloperEmployee(Employee,Developer):
    pass

mike = ADeveloperEmployee("python")
print(mike.intro())
```

这里我们定义一个类 `ADeveloperEmployee` 继承了 Employee，Developer，在没有定义初始化函数`__init__`默认调用第一个父类`__init__` 函数来初始化类实例属性，所以第一个父类为 Employee 时候，我们实例化时需要传入两个参数，如果之传入一个参数如下，系统就会抛出异常提示我们需要输入两个参数。

```python
Traceback (most recent call last):
  File "demo_03.py", line 19, in <module>
    mike = ADeveloperEmployee("python")
TypeError: __init__() missing 1 required positional argument: 'age'
```

如果

```python
class ADeveloperEmployee(Developer,Employee):
    pass

mike = ADeveloperEmployee("python")
print(mike.intro())
```

虽然实例化 `ADeveloperEmployee` 没有输出 `Employee` 方法，通过判断可以发现 `mike` 也是 `Employee` 和`Developer`



```python
print(isinstance(mike,Employee)) #True
print(isinstance(mike,Developer)) #True
```



```python
class Employee:
    def __init__(self,name,age):
        print("employee init()")
        self.name = name
        self.age = age

    def intro(self):
        return f"my name is {self.name} and {self.age} year old"
    
    def salary(self):
        return "salaray"

class Developer:
    def __init__(self,lang):
        print("developer init()")
        self.lang = lang

    def intro(self):
        return f"I'm a developer and can code {self.lang}"

class ADeveloperEmployee(Developer,Employee):
    pass
```



```python
mike = ADeveloperEmployee("python") #developer init()
print(mike.salary()) #salary
```

#### MRO(方法解析顺序)

```python
print(ADeveloperEmployee.__mro__)
```
方法解析顺序 (或 MRO) 告诉 Python 如何搜索继承的方法。有点类似于 Javascript 的原型链。每个类都有一个` .__mro__ `属性，通过这个属性检查方法解析的顺序。

```python
(<class '__main__.ADeveloperEmployee'>, <class '__main__.Developer'>, <class '__main__.Employee'>, <class 'object'>)
```

当调用 `mike` 的 `intro` 方法，就会沿着这个解析顺序先调用 Developer 的 `intro` 如果有就直接调用，如果没有就继续沿着的解析顺序看其他父类是否有该方法。

