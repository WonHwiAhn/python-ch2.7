# module name: mymod

print('mymod.py의 모듈이름: ' + __name__)

def main():
    print('최상의 모듈(독립실행)시, 출력됩니다.' )

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

if __name__ == '__main__':   # __name__이 main일경우에
    main()
else:
    print('mymod.py의 모듈 이름: ' + __name__)