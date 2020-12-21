x = int(input("Введіть значення х:"))
y = int(input("Введіть значення y:"))
z = int(input("Введіть значення z:"))

u = 0

if x >= y >= z:
    max1 = x
else:
    if y >= z:
        max1 = y
    else:
        max1 = z


if x+y >= x*y >= 4*z:
    max2 = x+y
else:
    if x*y >= 4*z:
        max2 = x*y
    else:
        max2 = 4*z


if x+y >= x*y >= x**2:
    max3 = x+y
else:
    if x*y >= x**2:
        max3 = x*y
    else:
        max3 = x**2


if  max3**2 >= 7 >= z**2:
    max4 = max3**2
else:
    if 7 >= z**2:
        max4 = 7
    else:
        max4 = z**2

u = (max1 + max2)/max4

print(u)
