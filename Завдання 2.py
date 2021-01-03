import math

def vector_length(coordinates):
    return (coordinates[0]**2 + coordinates[1]**2)**(1/2)


def kut(x1, y1, x2, y2, x3, y3, x4, y4):
    first_v = [x2-x1, y2-y1]
    second_v = [x4-x3, y4-y3]
    scalar_d = first_v[0] * second_v[0] + first_v[1] * second_v[1]
    return math.degrees(math.acos(scalar_d/(vector_length(first_v) * vector_length(second_v))))


def triangleType(x1, y1, x2, y2, x3, y3):
    kut_1 = kut(x1, y1, x2, y2, x1, y1, x3, y3)
    kut_2 = kut(x3, y3, x1, y1, x3, y3, x2, y2)
    kut_3 = kut(x2, y2, x1, y1, x2, y2, x3, y3)
    max_kut = max(kut_1, kut_2, kut_3)
    if max_kut > 90:
        return "Тупокуний"
    elif max_kut == 90:
        return "Прямокутний"
    return "Гострокутний"


print(triangleType(5, -5, 6, 0, 7, 1))



