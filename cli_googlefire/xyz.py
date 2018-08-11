import fire


value = 'hello'


if __name__ == '__main__':
    fire.Fire()


"""
> python3 xyz.py value
hello
> python3 xyz.py value upper
HELLO
> python3 xyz.py value upper lower
TypeError: upper() takes no arguments (1 given)

很不幸，内置的字符串对象似乎不支持链式调用，第一个upper倒是执行成功了。
不过fire提供了一个特殊的符号用来解决这个问题。

> python3 xyz.py value upper - lower
hello
> python3 xyz.py value upper - lower - upper
HELLO
> python3 xyz.py value upper - lower - upper -lower
hello

"""
