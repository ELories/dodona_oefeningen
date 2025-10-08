def coulombkracht(q1, q2, r):
    k = 8.988e9
    F = k * abs(q1 * q2) / (r ** 2)
    return round(F, 4)
