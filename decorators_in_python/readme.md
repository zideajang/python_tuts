在本次分享中，接下来将介绍什么是**装饰器(decorators)** 以及如何创建和使用装饰器。装饰器提供了一种调用高阶函数的简单语法。根据定义，装饰器是一个函数，接收函数并对函数的行为进行扩展，只是扩展并不改变函数原有行为。这听起来有点 confusing，但其实并不复杂，相信看过这边文章对装饰器会有全面深刻的认识，然后通过大量 example 巩固成果。



在正式开始之前我们通过一个小例子来感受一下装饰器带来好处，体验一下装饰器好处。

```python
import time

def slow_square(number):
    print(f"Sleeping for {number} seconds")
    time.sleep(number)
    return number**2

print(slow_square(3))
print(slow_square(3))
print(slow_square(3))
```

上面代码执行后，用` sleep` 模拟一个耗时操作，让线程休眠 3 秒钟。执行代码会每间隔 3 秒输出一个数字，其实这个函数输出结果都一样。



我们先不用关心具体`@functools.lru_cache(maxsize=128, typed=False)`参数含义，只要知道这个是装饰器，通过这个装饰器修饰上面函数`slow_square`后再次运行代码，效果只仅停留 3 秒后直接一口气输出三个 9。

```python
import time
import functools

@functools.lru_cache(maxsize=128, typed=False)
def slow_square(number):
    print(f"Sleeping for {number} seconds")
    time.sleep(number)
    return number**2

print(slow_square(3))
print(slow_square(3))
print(slow_square(3))
```



我们输出一下`functools.lru_cache`，可以看到其实所谓装饰器就是一个函数。

```python
print(functools.lru_cache) #<function lru_cache at 0x108fcd560>
```

### 函数(Functions)

在理解装饰器之前，需要做一些准备工作，首先理解函数是如何工作的。可以简单将函数，**一个函数根据给定的参数返回一个值**。下面是一个非常简单的例子。

```python
def add(num_1,num_2):
    return num_1 + num_2
```



一般来说，Python 中的函数也可能有副作用，而不仅仅是把输入转换为输出。`print()` 函数就是一个典型的例子，该函数返回 None 的同时有一个向控制台输出的副作用，IO 操作可以看成一个副作用。然而，为了理解装饰器，只要把函数看作是把给定的参数变成一个值的东西就足够了。



> 注意：在函数式编程中，大部分函数都是没有副作用的纯函数。虽然 python 并不像 Haskell 不是一种纯粹的函数式语言，但 Python 支持许多函数式编程的概念，包括将函数作为第一类对象，这一点和 Javascript 相似函数在语言里都是一等公民。



#### 函数式

在 Python 中，函数是第一类对象。这意味着函数可以像其他对象 (string, int, float, list, 等等) 一样作为参数传递和也可以作为返回值。

```python
print_proxy = print
```

函数可以赋值给一个变量

```python
def greet(name,printer=print):
    printer(f"hi {name}")
```

我们可以将 print 作为一个参数传递给 `greet`

```python
def reverse(text):
    print(text[::-1])

greet("hi decorations",printer=reverse)
```



#### 内嵌函数
我们可以在其他函数中定义内嵌函数，这样的函数被称为内部函数。下面函数 `prefix_factory` 定义一个内部函数 `prefix_print`。

```python
def prefix_factory(prefix):
    def prefix_print(text):
        print(f"{prefix}: {text}")
    return prefix_print
```

#### 函数作为返回值

对于高阶函数而言，可以将函数做返回值返回。
```python
def prefix_factory(prefix):
    def prefix_print(text):
        print(f"{prefix}: {text}")
    return prefix_print
```


### 简单的装饰器

现在你已经看到函数就像 Python 中的其他对象一样，好了我们已经对 python 函数有一定的认识了，现在就开始写一个 Python 装饰器。

```python
def before_and_after(func):
    def wrapper(text):
        print("BEFORE")
        func(text)
        print("AFTER")

    return wrapper
```



```python
def greet(text):
    print(f"hi {text}") 

greet = before_and_after(greet)
```

```python
greet("decorators")
```

```
BEFORE
hi decorators
AFTER
```



#### 语法糖

你上面装饰 `before_and_after()`的方式略显有些笨拙。显然不是什么优雅的方式来实现装饰器，出现了 3 次 `greet`函数名称。此外，装饰被隐藏在函数定义的下面。

不过 Python 允许你用  @  符号以更简单的方式使用装饰器，这种方式就是我们熟悉语法糖的方式。下面就是通过语法糖对 greet 进行装饰，功能上和之前的函数完全相同。

```python
def before_and_after(func):
    def wrapper(text):
        print("BEFORE")
        func(text)
        print("AFTER")

    return wrapper

@before_and_after
def greet(text):
    print(f"hi {text}")

greet("decorators")
```



### 重用装饰器

回顾一下，装饰器只是一个普通的 Python 函数。所有常用的便于重用的工具都是可用的。让我们把装饰器移到它自己的模块中，可以在许多其他函数中使用。

创建一个名为 decorators.py 的文件，内容如下。



```python
import random

def do_twice(func):
    def wrapper(*args,**kwargs):
        val_1 = func(*args,**kwargs)
        val_2 = func(*args,**kwargs)
        return (val_1,val_2)
    return wrapper

@do_twice
def roll_dice():
    return random.randint(1,6)


print(roll_dice())
```


在使用 Python 时，特别是在交互式 shell 中，一个很大的便利就是它强大的自省能力。自省是指一个对象在运行时了解其自身属性的能力。例如，一个函数知道它自己的名字和文档。



```python
>>> print
<built-in function print>

>>> print.__name__
'print'

>>> help(print)
Help on built-in function print in module builtins:
```

```python
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        res_1 = func(*args, **kwargs)
        res_2 = func(*args, **kwargs)
        return res_1, res_2
    return wrapper_do_twice
@do_twice
def guess_number():
    return random.randint(1,6)
```

```
guess_number.__name__ #'wrapper_do_twice'
```
```
help(guess_number)
```

当函数`guess_number()` 被装饰后，`guess_number()`对自己的身份也随之发生了变化，这一点让人有点 consufing。当调用 `guess_number.__name__`  查看函数身份时，输出不是 `guess_number` 而是 `do_twice()` 装饰器中的 `wrapper_do_twice()`内部函数。虽然并没有问题，不过我们希望返回的是 `guess_number` 而不是· `wrapper_do_twice()`

为了解决这个问题，可以装饰器应该使用 @functools.wraps 装饰器，这样就不会保留被装饰函数的信息。

```python
def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        res_1 = func(*args, **kwargs)
        res_2 = func(*args, **kwargs)
        return res_1, res_2
    return wrapper_do_twice
```
```
@do_twice
def guess_number():
    return random.randint(1,6)
```

```python
guess_number.__name__ #'guess_number'
```


### 应用装饰器的一些例子
让我们来看看几个更有用的装饰器的例子。你会注意到，它们主要遵循你到目前为止所学到的相同模式。

#### 计时器

```python
def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter() #1
        value = func(*args,**kwargs)
        end_time = time.perf_counter() #2
        run_time = end_time - start_time#3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer
```



```python
@timer
def slow_square(number):
    time.sleep(number)
    return number**2
```

```python
slow_square(3)
```

```python
Finished 'slow_square' in 3.0003 secs
9
```

上面这个装饰器大家自己看代码，代码比较简单也容易理解，所以也就不做过多解释，装饰器就是会输出装饰函数的执行耗时时间。

> 注意：如果你只是想了解你的函数的运行时间，上面实现的 @timer 装饰器是很好的选择。如果想对代码执行时间进行更精确的测量，可能 @timer 就无法满足，应该考虑标准库中的 timeit 模块。暂时禁用垃圾收集，并运行多个试验来消除函数调用的 noise。

#### 调试工具
接下来写一个调试装饰器，`@debug` 装饰器将在每次函数被调用时，打印函数的参数以及其返回值。

```python
def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
        
        signatre = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signatre})")
        
        value = func(*args,**kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug
```



- 创建一个位置参数的列表，通过`repr()`得到一个表示每个参数的优雅字符串
- 创建一个关键字参数的列表。`f-string` 将每个参数格式化为 `key=value`，其中的`!r` 指定符表示用 `repr()` 来表示值

```python
@debug
def slow_square(number):
    time.sleep(number)
    return number**2
```

```python
slow_square(3)
```
```
Calling slow_square(3)
'slow_square' returned 9
9
```


#### 慢节奏

下面这个例子可能看起来不是很有用。为什么想 Python 代码慢下来呢？最常见的用例可能是，对一个连续检查资源例如查看下载进度，这时候这个方法就可能会派上用场。

```python
def slow_down(func):
    @functools.wraps(func)
    def wrapper_slow_donw(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_donw
```

```python
@slow_down
def countdown(from_num):
    if from_num < 1:
        print("done")
    else:
        print(from_num)
        countdown(from_num - 1)
```


#### 注册机
Decorators don’t have to wrap the function they’re decorating. They can also simply register that a function exists and return it unwrapped. This can be used, for instance, to create a light-weight plug-in architecture:

装饰者不一定要包装他们所装饰的函数。也可以简单地注册一个函数到集合，然后直接返回函数。例如，这可以用来创建一个轻量级的插件架构。

```python
PLUGINS = dict()

def register(func):
    PLUGINS[func.__name__] = func
    return func

@register
def java_dev(name):
    return f"my name is {name} and I am Java Developer"

@register
def python_dev(name):
    return f"my name is {name} and I am Python Developer"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)
```

`@register` 装饰器只是在全局 `PLUGINS dict`中存储了一个对被装饰函数的引用。注意，在这个例子中，不必写一个包装函数或使用 `@functools.wraps`，因为返回的是未经任何修改的原函数

`randomly_greet()`函数会随机选择一个注册的函数来使用。注意，PLUGINS 字典已经包含了对每个注册为插件的函数对象的引用。


```python
randomly_greet("mike")
```

```
Using 'java_dev'
'my name is mike and I am Java Develope
```

<hr/>





到目前为止，你已经看到了如何创建简单的装饰器。你已经对什么是装饰器以及如何工作有了一定的理解。接下来将进一步探索更多的高级功能，包括如何使用下列功能

### 类的装饰器

有两种不同的方法可以在类上使用装饰器。就像之前介绍用装饰器修饰函数那样，来修饰类的一个方法，这也是当初引入装饰器的原因之一。

python 已经提供一些现成的装饰器用于修饰类的方法，例如` @classmethod`, `@staticmethod`, 和 `@property`。`@classmethod` 和 `@staticmethod` 装饰器用于定义类上方法，这些方法与该类的具体实例无关。`@property`装饰器是用来类属性的`getters`和`setters`的。展开下面的方框，看看使用这些装饰器的例子。

```python
class RequestSimulator:
    @debug
    def __init__(self, max_num):
        self.max_mun = max_num
    
    @timer
    def req(self,num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_mun)])
```

这里我们上一次分享中已经实现好的`@debug` 和`@timer`来修饰类中一些方法。

```python
req_simulator = RequestSimulator(1000)
```

```python
Calling __init__(<__main__.RequestSimulator object at 0x10a422c50>, 1000)
'__init__' returned None
```



```python
req_simulator.req(999)
```



```python
Finished 'req' in 0.3136 secs
```



```python
from dataclasses import dataclass

@dataclass
class Tut:
    title: str
    subTitle: str
```



语法的含义与函数装饰器相似。在上面的例子中，以通过写`Tut = dataclass(Tut)`来完成这个类装饰器。类的装饰器的通常可以看做元类(metaclass) 一种实现方式。通过类装饰器可以动态地改变一个类的定义。



>  元类就是创建类这种对象的东西。可以把元类称为“类工厂”，当然这里理解难免有些片面。

编写一个类装饰器与编写一个函数装饰器非常相似。唯一的区别是，装饰器将接收一个类而不是一个函数作为参数。事实上，在上面看到的所有装饰器都可以作为类装饰器。在一个类而不是一个函数上使用时，其效果可能不是你想要的。在下面的例子中，`@timer`装饰器被应用于一个类。

```python
@timer
class RequestSimulator:

    def __init__(self, max_num):
        self.max_mun = max_num
    
    
    def req(self,num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_mun)])
```



```python
req_simulator = RequestSimulator(1000) #Finished 'RequestSimulator' in 0.0000 secs
req_simulator.req(999)
```



装饰一个类并不能装饰类的方法。@timer 只是`RequestSimulator = timer(RequestSimulator)`的简写。在这里，@timer只输出实例化类所需的时间。



### 使用多个装饰器来装饰一个函数

可以通过在定义函数时在函数上堆叠多个装饰器，不过需要注意下顺序，也就是不同的嵌套关系，下面通过一个例子来解释修饰顺序不同所带来效果也不同。

```python
@debug
@do_twice
def greet(name):
    print(f"Hello {name}")
```



```python
greet("mike")
```

这里顺序，当输出 2 次`hello mike` 输入一次 debug 信息 `debug(do_twice(greet))`

```python
Calling greet('mike')
Hello mike
Hello mike
'greet' returned (None, None)
(None, None)
```



```python
@do_twice
@debug
def greet(name):
    print(f"Hello {name}")
```



```python
greet("mike")
```

函数输出两次时，都带有 debug 信息。

```python
Calling greet('mike')
Hello mike
'greet' returned None
Calling greet('mike')
Hello mike
'greet' returned None
(None, None)
```



### 装饰器的参数

最开始我们引入装饰器概念是用到一个例子中，装饰器就是带参数的，想一想之前定义`do_twice` 装饰器将装饰的函数执行两次，不过这里固定执行 2 次，是不是缺失了灵活性。我们需要指定多少次由使用装饰器的开发人员自己定义。

So far, the name written after the `@` has referred to a function object that can be called with another function. To be consistent, you then need `repeat(num_times=4)` to return a function object that can act as a decorator. Luckily, you [already know how to return functions](https://realpython.com/primer-on-python-decorators/#returning-functions-from-functions)! In general, you want something like the following:

到目前为止，写在@后面的名字已经指的是一个可以与另一个函数一起调用的函数对象。为了保持一致，你就需要` repeat(num_times=4) `返回一个可以作为装饰器的函数对象。幸运的是，你已经知道如何返回函数了 一般来说，你希望有如下的结果。

```python
@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")
```



```python
greet("mike")
```

查看输出

```python
Hello mike
Hello mike
Hello mike
Hello mike
```



```python
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args,**kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat
```

上面就是 repeat 实现，函数层层嵌套，下面部分就是我们之前熟悉如何实现一个对函数装饰的装饰器。

```python
	def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args,**kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
```



了实现带有参数装饰器，就在装饰器函数外面又套了一层，这个函数用于接受参数，返回一个装饰器从而实现带参数的装饰器。可以参阅[聊一聊 Python 中的闭包｜Python 主题月](https://juejin.cn/post/6990252189599924238)。同样，`decorator_repeat()`看起来和你之前写的装饰器函数完全一样，只是名字不同而已。`__repeat()`。如你所见，最外层函数返回一个对装饰器函数的引用。



在 `repeat()` 函数中，发生了一些微妙变化

-  将 `decorator_repeat()`定义为一个内部函数意味着 ` repeat()` 将引用一个函数对象  `decorator_repeat`。我们使用不带括号的 `repeat` 来引用函数对象。在定义带参数的装饰器时，添加括号是必不可少了。
- 在` repeat()` 本身中，`num_times` 这个参数似乎没有被使用。但通过传递 `num_times`，我们创建了一个闭包，`num_times` 的值被存储在其中，直到以后被 `wrapper_repeat()` 使用。一切准备就绪后，让我们看看结果是否符合预期。





### 两个全都要(带参数的装饰器和不带参数装饰器)


只要稍加注意，你也可以定义既可以使用参数也可以不使用参数的装饰器。大多数情况下，你不需要这样做，但有这种做好处就是代码更加灵活。

正如你在上一节看到的，当装饰器使用参数时，你需要添加一个额外的外层函数。现在需要做的是判断调用时是否有参数，分为两种情况。


因为只有在装饰器被无参数调用时，才会直接传入要装饰的函数，该函数必须是一个可选参数。这里使用关键字 `*` 接受中间所有参数，这意味着，装饰器的参数必须全部由关键字指定。

```python
def name(_func=None, *, kw1=val1, kw2=val2, ...):  # 1
    def decorator_name(func):
        ...  # Create and return a wrapper function.

    if _func is None:
        return decorator_name                      # 2
    else:
        return decorator_name(_func)               # 3
```



在这里，`_func`参数作为一个标记，注意到装饰器是否被带参数调用。这里的确有点绕，需要花费一些时间理解其中的 trick。

- 如果`name`的调用不带参数，那么装饰的函数将作为`_func`作为默认参数，这是 `_func` 是值的 。如果调用带有参数调用，那么`_func`将是`None`，而且一些关键字参数可能已经从它们的默认值中被改变。参数列表中的`*`意味着其余的参数不能作为位置参数被调用。
- 在装饰器被调用时有参数情况下，返回`decorator_name(_func)  ` 可以读取参数并返回一个函数的装饰器函数。
- 在该装饰器被调用时，没有参数情况下，立即将装饰器应用于该装饰的函数

使用上一节中`@repeat`装饰器上的这个模板，你可以写出以下内容。

```python
def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)
```



```python
@repeat
def greet(name):
    print(f"Hello {name}")
```



```python
@repeat(num_times=3)
def greet_developer(name):
    print(f"Hello {name} I'm a developer")
```



```python
greet("mike")
Hello mike
Hello mike
```



```python
greet_developer("mike")
Hello mike I'm a developer
Hello mike I'm a developer
Hello mike I'm a developer
```



### 状态装饰器

有时，拥有一个可以跟踪状态的装饰器是很有用的。作为一个简单的例子，我们将创建一个装饰器来计算一个函数被调用的次数。

> 注意：在开始之前，我们谈到了纯函数基于给定的参数返回一个值。有状态的装饰器则完全相反，其返回值将取决于当前的状态以及给定的参数。



```python
def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls
```



```python
@count_calls
def greet(name):
    print(f"Hello {name}")
```



```python
greet("mike")
Call 1 of 'greet'
Hello mike
```



```python
greet("tony")
Call 2 of 'greet'
Hello tony
```



### 类装饰器

维护状态的一般方法是使用类，现在我们就也用一个类作为装饰器重写状态装饰器中的 `@count_calls`例子。

回顾一下，装饰器的语法 `@my_decorator`只是一种更简单的说法，即`func = my_decorator(func)`。因此，如果` my_decorator` 是一个类，需要在其` .__init__()` 方法中把` func` 作为一个参数。此外，这个类的实例需要是可调用的，这样就可以代替被装饰的函数。

```python
class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self,func)
        self.func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)
```

为了使一个类的实例可以被调用，我们实现了特殊的`.__call__()` 方法。

```python
@CountCalls
def greet(name):
    print(f"Hello {name}")
```

```python
greet("mike")
Call 1 of 'greet'
Hello mike
```

```python
greet("tony")
Call 2 of 'greet'
Hello tony
```
