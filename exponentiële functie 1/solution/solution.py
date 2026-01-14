# Definitie van de functie:
# f(x) = a - 4 * (1/3)^(x/2)
def f(a, x):
    y = a - 4 * ((1/3) ** (x / 2))
    return round(y, 1)

a = float(input())
x = float(input())
y = f(a, x)
print(f"De bijhorende y-waarde is {y:.1f} en de asymptoot ligt op y={a:.1f}.")
