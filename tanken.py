import math

# Hoe vaak moet je tanken om op je bestemming te komen? 
# Je vertrekt met een volle tank, 
# je rijdt de tank precies leeg en 
# vult deze dan volledig. (je kunt dus overal tanken!)

# Schrijf een functie in Python die een integer teruggeeft met het aantal tankbeurten.
# De functie heeft als parameters: kilometers_per_liter, tankinhoud, te_rijden_afstand.

def tanken(kilometers_per_liter, tankinhoud, te_rijden_afstand):
    aantal_km_max = tankinhoud / kilometers_per_liter
    aantal_tankbeurten = te_rijden_afstand / aantal_km_max
    return math.ceil(aantal_tankbeurten)

km_per_l = int(input("Hoeveel hele km kan je rijden met 1 liter benzine? "))
inhoud_tank = int(input("Hoeveel hele liters kunnen er in de tank? "))
afstand = int(input("Wat is de afstand in hele km? "))

print(f"Je moet {tanken(km_per_l, inhoud_tank, afstand)} keer tanken.")
