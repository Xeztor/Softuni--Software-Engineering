import cmath
import math

c_num = complex(input())
print(math.sqrt(c_num.real**2 + c_num.imag**2))
print(cmath.phase(c_num))

