#/usr/bin/python3
# -*- coding:utf-8 -*-

#一个最不常用的选择是可以让函数调用可变个数的参数。这些参数被包装进一个元组（参见 元组和序列 ）。在这些可变个数的参数之前，可以有零到多个普通的参数:
def write_multiple_items(file,separator,*args):
    file.write(separator.join(args))

#通常，这些 可变 参数是参数列表中的最后一个，因为它们将把所有的剩余输入参数传递给函数。任何出现在 *args 后的参数是关键字参数，这意味着，他们只能被用作关键字，而不是位置参数:

>>> def concat(*args, sep="/"):
... return sep.join(args)
...
>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>> concat("earth", "mars", "venus", sep=".")
'earth.mars.venus
