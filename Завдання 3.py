import random

def x(i):
    if i == 0:
        return 0
    elif i == 1 or i == 2:
        return 9
    else:
        return (x(i-1) + 4*x(i-3))

n = int(input("n="))

print(f"x{n}={x(n)}")


