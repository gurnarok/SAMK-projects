import math as m
import decimal as d
# Generate Euler number by summing 1 over factorial of n.
# More info @ https://en.wikipedia.org/wiki/E_(mathematical_constant)
n = int(input("How many factorials? "))
tSum = 0
for i in range(n+1):
    f = m.factorial(i)
    # Using Decimal, I can get much accurate result
    tSum = d.Decimal(tSum) + d.Decimal((1/f))
    d.getcontext().prec = 200
    print(f'i = {i:3d}  :  sum={tSum:.200f}')
