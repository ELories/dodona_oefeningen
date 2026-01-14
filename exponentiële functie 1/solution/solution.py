# Definitie van de functie:
# f(x) = a - 4 * (1/3)^(x/2)
def f(a,x):
    y = a - 4 * ((1/3) ** (x / 2))
    return(round(y,1))

a = float(input("Voer een waarde voor a in: "))
x = float(input("Voer een waarde voor x in: "))
y = f(a,x)
print("De bijhorende y-waarde is", y,"en de asymptoot ligt op y =",a,".")
