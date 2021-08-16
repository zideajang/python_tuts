Python’s filter() is a built-in function that allows you to process an iterable and extract those items that satisfy a given condition. This process is commonly known as a filtering operation. With filter(), you can apply a filtering function to an iterable and produce a new iterable with the items that satisfy the condition at hand. In Python, filter() is one of the tools you can use for functional programming.



Python 的 `filter()` 是一个内置的函数，允许你处理一个迭代器并提取那些满足给定条件的项目。这个过程通常被称为过滤操作。使用 `filter()` ，可以将过滤函数应用于一个迭代器，返回一个新的迭代器，其中包含满足当前条件的元素。在 Python 中，`filter() `是可以用来进行函数式编程的工具之一，大多数人在演示函数式编程都会解释 filter、map 和 reduce。

With this knowledge, you’ll be able to use filter() effectively in your code. Alternatively, you have the choice of using list comprehensions or generator expressions to write more Pythonic and readable code.

有了这些知识，就能在代码中有效地使用` filter() `。另外，也可以选择使用列表理解或生成器表达式来编写更多的 Pythonic 和可读的代码。为了更好地理解 `filter()`，需要对迭代器、for 循环、函数和 `lambda`函数这些知识有所了解。

In functional programming, functions often operate on arrays of data, transform them, and produce new arrays with added features. There are three fundamental operations in functional programming:

Mapping applies a transformation function to an iterable and produces a new iterable of transformed items.
Filtering applies a predicate, or Boolean-valued, function to an iterable and generates a new iterable containing the items that satisfy the Boolean condition.
Reducing applies a reduction function to an iterable and returns a single cumulative value.

在函数式编程中，函数经常对数据数组进行操作，对进行转换，并产生具有附加功能的新数组。在函数式编程中，有三种基本操作:

- **映射(Mapping)**:  将转换函数应用于一个迭代器，并产生一个由转换后的项目组成的新迭代器
- **过滤(Filtering)**:  将一个预估或布尔值函数应用于一个迭代器，并生成一个包含满足布尔条件的项目的新的迭代器。
- **迭代(Reducing)**:  将一个 reduce 函数应用于一个可迭代项，并返回一个的累积值。

Python 并没有受到函数式语言的严重影响，而是受到命令式语言的影响。然而，它提供了几个允许你使用函数式的功能。

- 匿名函数
- map()函数
- filter() 函数
- reduce()函数

Python 中的函数是第一类对象，这意味着你可以像对待其他对象那样传递它们。你也可以把它们作为其他函数的参数和返回值。接受其他函数作为参数或返回函数 (或两者兼而有之) 的函数被称为高阶函数，这也是函数式编程中的一个理想特性。

在本教程中，你将学习 filter()。这个内置函数是 Python 中比较流行的函数式工具之一。