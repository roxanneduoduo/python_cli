"""
类 vs 对象
暴露类和暴露对象似乎没有任何区别，那到底该选哪种比较优雅呢？
这个要看类的构造器有没有参数，如果是不带参数的构造器，那么类和对象的暴露是没有区别的，
但是如果类的构造器有参数，那就不一样了，下面我们改造一下Maths类，增加一个放大系数。
"""
import math
import fire

class Maths(object):

    def __init__(self, coeff):
        self.coeff = coeff

    def pi(self, n):
        s = 0.0
        for i in range(n):
            s += 1.0/(i+1)/(i+1)
        return self.coeff * math.sqrt(6*s)

    def fact(self, n):
        s = 1
        for i in range(n):
            s *= (i+1)
        return self.coeff * s


if __name__ == '__main__':
    # exposureclass
    # fire.Fire(Maths)

    # exposure object
    fire.Fire(Maths(coeff=2))

"""
如果改成暴露对象，那么放大系数就是在代码里写死的，无法在命令行进行参数定制了。
这就是暴露对象和暴露类的差别，似乎暴露类在功能上更强大一些。
"""
