"""暴露字典"""

import math
import fire


    
def pi(n):
    s = 0.0
    for i in range(n):
        s += 1.0/(i+1)/(i+1)
    return math.sqrt(6 * s)

def fact(n):
    s = 1
    for i in range(n):
        s *= (i+1)
    return s


if __name__ == '__main__':
    fire.Fire({
	"pi[n]": pi
    })
