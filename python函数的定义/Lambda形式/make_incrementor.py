出于实际需要，有几种通常在函数式编程语言例如 Lisp 中出现的功能加入到了
Python。通过 lambda 关键字，可以创建短小的匿名函数。这里有一个函数返回它
的两个参数的和： lambda a, b: a+b 。 Lambda 形式可以用于任何需要的函数对
象。出于语法限制，它们只能有一个单独的表达式。语义上讲，它们只是普通函数
定义中的一个语法技巧。类似于嵌套函数定义，lambda 形式可以从外部作用域引
用变量:
>>> def make_incrementor(n):
... return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
上面的示例使用 lambda 表达式返回一个函数。另一个用途是将一个小函数作为参
数传递:
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
