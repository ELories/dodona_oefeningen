# Definitie van de functie:
# f(x) = a - 4 * (1/3)^(x/2)
def f(a, x):
    """Teruggeven: y afgerond op 1 decimaal (zoals in je expression-tests)."""
    y = a - 4 * ((1/3) ** (x / 2))
    return round(y, 1)


# I/O alleen in main-guard zodat import veilig is voor expression-tests
if __name__ == "__main__":
    # Gebruik input() zonder prompt zodat automatische tests (stdin/stdout) werken.
    a = float(input().strip())
    x = float(input().strip())
    y = f(a, x)
    print(f"De bijhorende y-waarde is {y:.1f} en de asymptoot ligt op y={a:.1f}.")
