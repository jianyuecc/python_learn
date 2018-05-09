最常用的一种形式是为一个或多个参数指定默认值。这会创建一个可以使用比定义
时允许的参数更少的参数调用的函数，例如:
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
while True:
ok = input(prompt)
if ok in ('y', 'ye', 'yes'):
return True
if ok in ('n', 'no', 'nop', 'nope'):
return False
retries = retries ‐ 1
if retries < 0:
raise OSError('uncooperative user')
print(complaint)
这个函数可以通过几种不同的方式调用:
只给出必要的参数:
ask_ok('Do you really want to quit?')
给出一个可选的参数:
ask_ok('OK to overwrite the file?', 2)
或者给出所有的参数:
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
这个例子还介绍了 in 关键字。它测定序列中是否包含某个确定的值。
默认值在函数 定义 作用域被解析，如下所示:
i = 5
def f(arg=i):
print(arg)
i = 6
f()
将会输出 5 。
重要警告: 默认值只被赋值一次。这使得当默认值是可变对象时会有所不同，比如
列表、字典或者大多数类的实例。例如，下面的函数在后续调用过程中会累积（前
面）传给它的参数:
def f(a, L=[]):
L.append(a)
return L
print(f(1))
print(f(2))
print(f(3))
这将输出:
[1]
[1, 2]
[1, 2, 3]
如果你不想让默认值在后续调用中累积，你可以像下面一样定义函数:
def f(a, L=None):
if L is None:
L = []
L.append(a)
return L

