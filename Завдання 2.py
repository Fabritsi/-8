import math
x1 = float(input('Введіть координати х1:')) #точ.А
y1 = float(input('Введіть координати y1:'))

x2 = float(input('Введіть координати х2:')) #точ.B
y2 = float(input('Введіть координати y2:'))

x3 = float(input('Введіть координати х3:')) #точ.C
y3 = float(input('Введіть координати y3:'))

v_x1 = x2 - x1 #AB
v_y1 = y2 - y1

v_x11 = x1 - x2 #BA
v_y11 = y1 -y2

v_x2 = x3 - x2 #BC
v_y2 = y3 - y2

v_x22 = x2 - x3 #CB
v_y22 = y2 - y3

v_x3 = x1 - x3 #CA
v_y3 = y1 - y3

v_x33 = x3 - x1 #AC
v_y33 = y3 - y1

cos_A = ((v_x1 * v_x33) + (v_y1 * v_y33))/((math.sqrt((v_x1**2)*(v_y1**2)))*(math.sqrt((v_x33**2)*(v_y33**2))))

cos_B = ((v_x11 * v_x2) + (v_y11 * v_y2))/((math.sqrt((v_x11**2)*(v_y11**2)))*(math.sqrt((v_x2**2)*(v_y2**2))))

cos_C = ((v_x3 * v_x22) + (v_y3 * v_y22))/((math.sqrt((v_x3**2)*(v_y3**2)))*(math.sqrt((v_x22**2)*(v_y22**2))))

kut1 = math.acos(cos_A)
kut2 = math.acos(cos_B)
kut3 = math.acos(cos_C)

gkut1 = math.degrees(kut1)
gkut2 = math.degrees(kut2)
gkut3 = math.degrees(kut3)

if gkut1 > 90 or gkut2 > 90 or gkut3 > 90:
    print("Трикутник тупокутний")
else:
    if gkut2 < 90 or gkut1 < 90 or gkut3 < 90:
        print("Трикутник гострокутний")
    else:
        if gkut2 == 90 or gkut1 == 90 or gkut3 == 90:
            print("Трикутний прямокутний")
        else:
            print("Такого трикутника не існує")


