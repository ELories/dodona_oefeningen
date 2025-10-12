# Bereken de omtrek en de oppervlakte van een driehoek
from math import sqrt
basis = 5.0
hoogte = 8.0

schuine_zijde = sqrt(basis**2 + hoogte**2)

omtrek = round(basis + hoogte + schuine_zijde, 1)
oppervlakte = round((basis * hoogte) / 2)

print("De omtrek van de driehoek is gelijk aan", omtrek, "cm.")
print("De oppervlakte van de driehoek is gelijk aan", oppervlakte, "cm².")
