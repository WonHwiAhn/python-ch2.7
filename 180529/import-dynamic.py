# 동적(dynamically) import를 위한 __import__함수 사용

import sys

sys.path.append('../python-modules')

m = __import__('mymath')

print(m.pi)
print(m.add(10, 20))
print(m.area_circle(10))

