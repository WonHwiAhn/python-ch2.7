# module name: mymodule2

import mymodule

def power(x, y):
    r = 1
    for i in range(y):
        r = mymodule.multiply(r, x)
    return r

print('mymod2.py의 모듈이름:' + __name__)
