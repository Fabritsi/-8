def max(A, B, C):
    if A > B > C:
        return A
    elif B > A > C:
        return B
    else:
        return C

x = int(input("x="))
y = int(input("y="))
z = int(input("z="))
d = (max(x, y, z) + max((x + y), x*y, 4 * z)) / (max((max((x + y), x * y, x ** 2)) ** 2, 7, z ** 2))
print("Відповідь:", d)
