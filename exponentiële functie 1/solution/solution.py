# Definitie van de functie:
# f(x) = 5 - 4 * (1/3)^(x/2)
def f(x):
    y = 5 - 4 * ((1/3) ** (x / 2))
    return(round(y,1))

x = float(input("Voer een waarde voor x in: "))
y = f(x)
print("")
