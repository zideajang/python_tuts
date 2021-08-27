## 函数式编程在数据科学的应用
函数式编程现在热度虽然稍减，但是还是有很多人去讨论函数式编程。函数式编程并不是什么新的东西，在很早就被提出，所以再一次回到人们眼前成为热点，也是自然而然一件事，因为今天的程序越来越复杂，为了便于扩展和可测试，这时函数式编程就显得尤为重要，因为函数式编程对于同一个输入其输出是确定的。为降低成本我们就需要把一些确定的和一些不确定的进行分离，对于应用内部我们只需要把可以确定做好，而不必过多关心哪些不确定。在生活中也是如此，我们只把自己力所能及做好就行。

那么什么是函数式编程，python 这门语言是否支持函数式编程，如何将函数式编程应用科学研究上。这是今天我们要展开讨论的几个话题。

### 什么是函数式编程
有时候不喜欢用一个概念去解释另一个概念。那么什么是函数，$f(x) = 2x$ 这是一个简单函数，自己浅显理解就是两个集合间的映射。可以将函数式编程理解为一个计算单元


- 函数式编程是一种编程风格
- 可以用 lambda calulus 来解释函数式编程，

#### 函数式编程的历史
- John McCarthy 发明了 LISP 是早期支持
- John Backus 提出函数式编程的定义

#### 函数式编程有哪些风格
- 不变性(无侧边效应)
- 函数组合
- 无状态
- 平行


### 函数式编程是拥抱数据科学
- 函数式编程更适合 ELT
- 

### 不可变(immutable)的数据
我们都希望事物或人是不变，喜欢一个人，就从一而终海枯石烂也不改变。但是现实往往是事与愿违，但是相信世上还是有这样简单而且纯粹的爱情。

#### python 对不可变数据的支持
```python
s = "hello"
s + "wolrd"
s # hello
```

#### numpy 对不可变数据的支持
```python
import numpy as np
a = np.array([2,3,4,5])
a.append(0)
```
对于 numpy 这个在数据科学中广泛应用的数据库来说，numpy 对于不可变数据这一函数式编程的特性也有良好支持，例如一旦完成`numpy array` 的创建之后，我们就无法
在对这个设个数组添加新的元素，会抛出这个异常`AttributeError: 'numpy.ndarray' object has no attribute 'append'`。这源于 numpy 的实现设计，

```python
a[0] = 1
a # array([1, 3, 4, 5])
```
当我们对于 ndarray 进行如下设置，就无法 
```python
a.flags.writeable = False
```
在设置了`a.flags.writeable = False` 后在去修改 `a[0]=1` 就会抛出这个异常 `ValueError: assignment destination is read-only`。这是要修改这个 `ndarray`
就需要用 `copy` 命令赋值出一份进行修改。


#### pandas 对不可变性的支持

可能你在使用 pandas 并没有注意和特意去设置这个参数，这个参数就是`inplace`在一些，默认情况`inplace=False`也就是我们对 DataFrame 进行修改不会反应到原有数据，而是根据修改
生成一个新的 DataFrame 这说明 pandas 也具有良好的不可变性(immutable)

```python
tut_dictionory = {
    'name': ['basic machinelearning', 'deep learning', 'efficient python programming'],
    'price': ['120.0', '300.0', None],
    'level': [0, 1, 2]
}
df = pd.DataFrame(tut_dictionory)
df.head()
```

- df.replace(inplace=True)
- df.dropna(inplace=True)
- df.drop(inplace=True)
- df.rename(inplace=True)
- df.fillna(inplace=True)


### 纯函数
首先纯函数，所谓纯函数就是输入相同参数函数返回结果总是相同的，没有侧边效应，可以理解数学意义上函数。要理解什么是纯函数，其他内容都比较容易理解，就是什么是侧边效应相对来说
不算好理解，接下来就重点介绍一下什么是侧边效应，相信大家理解了什么是侧边效应，自然而然就理解了什么是纯函数。



#### 什么是侧边效应(side effects)
可能大家还不了解什么是侧边效应，我们先看一个小例子，然后罗列出哪些算是侧边效应
```python
global_list = []

def non_pure_add1_func(x):
    global_list.append(x)
    return x+1
```
这个实例虽然很简单，不过也足够说明问题，就是`non_pure_add1_func` 函数除了将 `x +1 ` 返回作为函数输出，还更新了一下全局变量。
所以我们需要保持函数 pure 不要在里面做一些类似更新全局状态，或者 I/O 方面的工作。

#### 侧边效应包括
- 任何 I/O 操作(网络，文件系统，输入输出设备)
- 抛出异常
- 更新对象状态
- 更新全局状态

#### 纯函数
理解什么是侧边效应，也理解了什么是纯函数。那么我们为什么需要纯函数，他能给我们带来哪些好处呢? 首先纯函数比较直观具有确定性，而且通过随意组合可以得到新的纯函数，
便于测试和缓存，易于并行计算，因为每一个函数都是独立不涉及数据一致性或更新状态的问题。

##### 组合
```python
def add(a,b):
    return a + b
def subtract(x,y):
    return add(x,y *-1)
```

### 引用透明(Referential transparency)
### 函数组合
- 高阶函数
- 函数是第一个公民

### 命令式(imperative)和声明式(declarative)
- 命令式告诉程序做什么同时还要告诉程序怎么做
- 声明式只需要告诉程序做什么即可

例如矩阵点乘

#### 命令式实现
```python
A = [[1,-1,2],[0,3,1]]
x = [2,1,0]
result = []
row_count = 0
for row in A:
    partial_result = 0
    for i in range(len(row)):
        a_elem = row[i]
        x_elem = x[i]
        partial_result += (a_elem * x_elem)
    result.append(partial_result)
    row_count += 1
    
result
```
#### 函数式实现
```python
A_arr = np.array([[1,-1,2],[0,3,1]])
x_arr = np.array([2,1,0])
A_arr @ x_arr

```

### map、filter 和 reduce
提到 numpy 的数组，少不了这 3 个方法，这是  3 (Map, Filter 和 Reduce)个有助于理解函数式编程风格的函数。将逐一讨论这 3 个方法，并了解在 python 以及 numpy 中的如何使用这些方法。
#### Map
Map 会对集合每一个元素进行操作或者说转换，操作或者转换后的元素组成一个新的集合
```python
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
```
在 numpy 中，用 list 进行 map 操作就更加容易，只需要`items**2` 就会对每个元素进行操作。
```python
items = np.array([1,2,3,4,5])
items**2
```

#### Filter
过滤器创建一个元素列表，其中一个操作每个元素函数会bool 类型值，真则会保留该元素到新列表
```python
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
```

```python
number_list_arr = np.array(range(-5,5))
number_list_arr[number_list_arr>0] # array([1, 2, 3, 4])
```

#### Reduce

Reduce 是一个非常有用的函数，用于对一个列表进行一些计算并返回结果。不断在在上一次计算结算基础上进行结算来累加。看看 js 的 redux 好像就是基于 reduce 实现

```python
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
```

```python
np.multiply.reduce([2,3,5])
```