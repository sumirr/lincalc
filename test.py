# define a function to calculate the projection between two vectors using sympy

from sympy import *

def projection(a, b):
    return (a.dot(b) / b.dot(b)) * b

# define a function to calculate the reflection between two vectors using sympy
def reflection(a, b):
    return (2 * a.dot(b) / b.dot(b)) * b - a

# define a function to calculate the angle between two vectors using sympy
def angle(a, b):
    return acos(a.dot(b) / (a.magnitude() * b.magnitude()))

# define a function to calculate the cross product between two vectors using sympy
def cross(a, b):
    return Matrix([a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]])

# define a function to calculate the dot product between two vectors using sympy
def dot(a, b):
    return a.dot(b)

# define a function to calculate the magnitude of a vector using sympy
def magnitude(a):
    return a.magnitude()

# define a function to calculate the unit vector of a vector using sympy
def unit(a):
    return a.normalize()

# define a function to calculate the addition of two vectors using sympy
def add(a, b):
    return a + b

# define a function to calculate the subtraction of two vectors using sympy
def subtract(a, b):
    return a - b

# define a function to calculate the scalar multiplication of a vector using sympy
def scalar(a, b):
    return a * b

# define a function to calculate the vector multiplication of two vectors using sympy
def vector(a, b):
    return a * b

# define a function to calculate the vector division of two vectors using sympy
def divide(a, b):
    return a / b

# define a function to calculate the vector power of a vector using sympy
def power(a, b):
    return a ** b

# define a function to calculate the vector square root of a vector using sympy
def sqrt(a):
    return a ** (1/2)

# define a function to calculate the vector cube root of a vector using sympy
def cbrt(a):
    return a ** (1/3)

# define a function to calculate the vector square of a vector using sympy
def square(a):
    return a ** 2

# define a function to calculate the vector cube of a vector using sympy
def cube(a):
    return a ** 3

# define a function to calculate the vector inverse of a vector using sympy
def inverse(a):
    return 1 / a

# define a function to calculate the vector absolute value of a vector using sympy
def abs(a):
    return a.applyfunc(lambda x: x if x > 0 else -x)

# define a function to calculate the vector factorial of a vector using sympy
def factorial(a):
    return a.applyfunc(lambda x: factorial(x))

# define a function to calculate the vector log of a vector using sympy
def log(a):
    return a.applyfunc(lambda x: log(x))

# define a function to calculate the vector log base 10 of a vector using sympy
def log10(a):
    return a.applyfunc(lambda x: log(x, 10))

# define a function to calculate the vector log base 2 of a vector using sympy
def log2(a):
    return a.applyfunc(lambda x: log(x, 2))

# define a function to calculate the vector natural log of a vector using sympy
def ln(a):
    return a.applyfunc(lambda x: ln(x))

# define a function to calculate the vector sine of a vector using sympy
def sin(a):
    return a.applyfunc(lambda x: sin(x))

# define a function to calculate the vector cosine of a vector using sympy
def cos(a):
    return a.applyfunc(lambda x: cos(x))

# define a function to calculate the vector tangent of a vector using sympy
def tan(a):
    return a.applyfunc(lambda x: tan(x))

# define a function to calculate the vector cotangent of a vector using sympy
def cot(a):
    return a.applyfunc(lambda x: cot(x))


