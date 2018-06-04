# 다양한 import 방법

# Way 1.
# import math
# print(math.sin(math.pi/6), math.cos(math.pi/6))

# Way 2.
# 같은이름의 모듈을 사용할 경우 마지막꺼로 덮히게 된다. [alias로 해결가능]
# from math import pi, sin, cos
# from mymath import pi
# print(sin(pi/6), cos(pi/6))

# Way 3.
# from math import *
# import mymath as m
# print(sin(pi/6), cos(m.pi/6))

# Way 4.
from math import sin as mysin, cos as mycos
from mymath import pi
print(mysin(pi/6), mycos(pi/6))