#/usr/bin/python3
# -*- coding=utf8 -*-
#最常用的一种形式是为一个或多个参数指定默认值。这会创建一个可以使用比定义时允许的参数更少的参数调用的函数，例如：
def ask_ok(prompt,retries=4,complaint='Yes or no,please!'):
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            quit()
            return True
        if ok in ('n','no','nop','nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)

#这个例子还介绍in关键字。他测定序列中是否包含某个确定的值
#三种调用的方式
ask_ok('Do you really want to quit?')

ask_ok('Ok to overwrite the file?',2)

ask_ok('Ok to overwrite the file?',2,'Come on,only yes or no!')


