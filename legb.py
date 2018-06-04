# LEGB Rules

# 1. Local
# 2. Enclosing Function(내포한 함수)
# 3. Global
# 4. Bulit-in

a = 1   # Global

def f():
    b = 1   # Enclosing

    def g():
        b = 100 # Local
        print(b)
        print(__name__) # Bulit-in

    g()

f()