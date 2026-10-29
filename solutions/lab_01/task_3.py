#эксперимент а
def f(n):
    print(n, type(n))

x = 17
y = 5

f(x + y)
f(x - y)
f(x * y)
f(x / y)
f(x // y)
f(x % y)
f(x ** y)


#эксперимент b
a = 2 ** 1000
print(a)


#эксперимент c
import math
result = 0.1 + 0.2
print(result)
print(result == 0.3)
print(result - 0.3)
print(math.isclose(result, 0.3))


#эксперимент d
f(int("42"))
f(float("3.14"))
f(str(2026))
f(bool(0))
f(bool(-1))
f(bool(""))
f(bool("False"))
a = complex(2, -3)
f(a)
print(a.real)
print(a.imag)
print(type(False))