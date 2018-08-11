"""暴露函数"""

import math
import fire


    
def pi(n):
    s = 0.0
    for i in range(n):
        s += 1.0/(i+1)/(i+1)
    return math.sqrt(6 * s)


if __name__ == '__main__':
    fire.Fire(pi)
