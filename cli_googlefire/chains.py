import fire


class Chain(object):
    
    def __init__(self):
        self.value = 1

    def incr(self):
        print('incr', self.value)
        self.value += 1
        return self

    def decr(self):
        print('desr', self.value)
        self.value -= 1
        return self

    def get(self):
        return self.value

if __name__ == '__main__':
    fire.Fire(Chain)

""" python3 chains.py incr incr incr decr decr get"""
