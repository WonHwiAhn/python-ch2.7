# infinitely import test

import sys
import mod_a

print('import infinitely')
print(sys.modules)

# print(sys.modules)
for key in sys.modules.keys():
    print(key)
