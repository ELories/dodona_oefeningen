# Berekening van het aantal rollen behangpapier
lengte = 25
hoogte = 2.5
lengte_rol = 10
hoogte_rol = 0.52
prijs_rol=24.95
aantal_rollen=lengte*hoogte//(lengte_rol*hoogte_rol)
prijs=aantal_rollen*prijs
print("Je moet", round(aantal_rollen), "rollen behangpapier kopen.")
print("De kostprijs bedraagt", prijs.)
