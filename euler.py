import math as m

# Generate Euler number by summing 1 over factorial of n.
# More info @ https://en.wikipedia.org/wiki/E_(mathematical_constant)
n = int(input("How many factorials? "))
tSum = 0
for i in range(n+1):
    f = m.factorial(i)
    tSum = tSum + (1/f)
    # Does not change after n=17. Need to test other options.
    print(f'i = {i:3d}  :  sum={tSum:.100f}')
