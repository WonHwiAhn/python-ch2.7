# mymath module test
import sys

# 절대경로
sys.path.append('/cafe24/PycharmProject/python-modules')

# 상대경로
# sys.path.append('../python-modules')

import mymath

print(mymath.add(10, 20))
print(mymath.area_circle(10))
