#/usr/bin/python3
# -*- coding:utf-8 -*-
#函数可以通过关键字参数的形式来调用，形如 keyword = value 。例如，以下的函数：

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("‐‐ This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("‐‐ Lovely plumage, the", type)
    print("‐‐ It's", state, "!")


#接受一个必选参数(voltage)以及三个可选参数(state,action，和 type)。可以用以下的任一方法调用:

parrot(1000) # 1 positional argument
parrot(voltage=1000) # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM') # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000) # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump') # 3 positional arguments
parrot('a thousand', state='pushing up the daisies') # 1 positional, 1 keyword

#不过以下几种调用时无效的

parrot() # required argument missing
parrot(voltage=5.0, 'dead') # non‐keyword argument after a keyword argument
parrot(110, voltage=220) # duplicate value for the same argument
parrot(actor='John Cleese') # unknown keyword argument

#引入一个形如 **name 的参数时，它接收一个字典（参见 Mapping Types — dict），该字典包含了所有未出现在形式参数列表中的关键字参数。这里可能还会组合使用一个形如 *name （下一小节详细介绍） 的形式参数，它接收一个元组（下一节中会详细介绍），包含了所有没有出现在形式参数列表中的参数值（ *name 必须在 **name 之前出现）。 例如，我们这样定义一个函数:

def cheeseshop(kind, *arguments, **keywords):
    print("‐‐ Do you have any", kind, "?")
    print("‐‐ I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("‐" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

#它可以像这样调用:

cheeseshop("Limburger", "It's very runny, sir.",
	   "It's really very, VERY runny, sir.",
	   shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

#当然它会按如下内容打印:

‐‐ Do you have any Limburger ?
‐‐ I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐
client : John Cleese
shopkeeper : Michael Palin
sketch : Cheese Shop Sketch

#注意在打印关键字参数之前，通过对关键字字典 keys() 方法的结果进行排序，生成了关键字参数名的列表；如果不这样做，打印出来的参数的顺序是未定义的。


