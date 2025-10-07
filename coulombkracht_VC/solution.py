k = 8.99e9
q1 = 2.0e-6
q2 = 3.0e-6
r = 5.0e-2  # 0.05 meter

F = k * abs(q1 * q2) / r**2
print(f"De elektrische kracht is gelijk aan {F:.2f} N.")
