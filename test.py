import time

# naam = input("Wat is je naam? ")
# if naam == "yilmaz":
#     print("Je hebt gratis bezorging.")
# print("Hartelijk welkom", naam, "")


# b = 5 
# if b == 5:
#     a = input("Vul wat in")
# a = a
# if a == "a":
#     print("Deze if is true")

got_boss_key = False
items_player = ["schild"]
deurkeuze_kamer_4 = input("Je ziet 2 deuren. Wil je (Enter) rechtdoor gaan of (a) de rechtse deur nemen? ")
while True:
    if deurkeuze_kamer_4 == "":
        if got_boss_key or "bom" in items_player:
            print("Je hebt het slot van de deur af kunnen halen.")
            print("")
            time.sleep(2)
            break
        else:
            print("Oei je hebt niks om de deur mee te openen.")
            time.sleep(2)
            print("Je loopt door de deur die wel open is.")
            deurkeuze_kamer_4 = "a"
            time.sleep(2)
    if deurkeuze_kamer_4 == "a":
        time.sleep(2)
        # === [kamer 12] === #
        print("Je opent de deur. Je valt in een diepe put. Hier kom je niet uit en je bent te gewond om verder door te gaan.")
        print("Game Over")
        break
        # exit()
print('')
time.sleep(1)