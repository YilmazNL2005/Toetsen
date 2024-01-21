import time, math
from random import randint
import random

player_attack = 1
player_defense = 0
player_health = 3
player_bank_rupee = 0

got_key = False

# Deze code (regel 9 en 10) zijn voor kamer 2
eerste_getal = randint(10, 25)
tweede_getal = randint(-5, 75)
som = eerste_getal + tweede_getal


# === [kamer 1] === #

print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)


# === [kamer 7] === #

# De speler kan nu, na het vinden van de ruppee, 
# kiezen welke kant deze op wil (bijvoorbeeld rechtdoor of naar rechts).

print("Je stapt door de deur en ziet een Rupee op de grond liggen.")
print("Wat je ermee kunt is nog een raadsel, je neemt het in ieder geval mee.")
player_bank_rupee += 1
print(player_bank_rupee)
deurkeuze_kamer_7 = input("Je ziet 2 deuren. (a) Wil je rechtdoor of (Enter) wil je naar rechts? ")
print('')
time.sleep(1)


# === [kamer 2] === #

if deurkeuze_kamer_7 == "a":
    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print('Het standbeeld heeft een sleutel vast.')
    print('Op zijn borst zit een numpad met de toetsen 0 t/m 9.')
    print(f'Daarboven zie je een som staan ', eerste_getal, " + ", tweede_getal, ' ? ')
    antwoord = int(input('Wat is het antwoord? '))

    if antwoord == som:
        print('Het stadbeeld laat de sleutel vallen en je pakt het op')
        got_key = True
    else:
        print('Er gebeurt niets....')

    print('Je ziet een deur achter het standbeeld.')
    print("Maar links zie je ook een deur.")
    deurkeuze_kamer_2 = input("Welke van de twee deuren wil je nemen? (a) De deur achter het stanndbeeld of (Enter) de deur rechts van het standbeeld? ")
    print('')
    time.sleep(1)


# === [kamer 6] === #

    zombie_attack = 1
    zombie_defense = 0
    zombie_health = 2
    # entiteiten_lijst = [player_health, zombie_health]
    if deurkeuze_kamer_2.lower() == "a":
        zombie_hit_damage = (zombie_attack - player_defense) # Dit is de hoeveelheid schade een zombie kan toebrengen aan de speler PER SLAG.
        player_hit_damage = (player_attack - zombie_defense)
        if zombie_hit_damage <= 0:
            print('Jij hebt een te goede verdediging voor de zombie, hij kan je geen schade toebrengen.')
        else:
            while zombie_health > 0 or player_health > 0:
                zombie_health -= player_hit_damage
                print(zombie_health, "Zombie")
                if zombie_health > 0:
                    player_health -= zombie_hit_damage
                    print(player_health, "Speler")
                    if player_health > 0:
                        continue
                    else:
                        print("Helaas je bent te gewond om verder door te gaan.")
                        print("Game Over")
                        exit()
                        # break
                else:
                    print("Je hebt de zombie gedood. ")
                    print(f'Je health is nu {player_health}.')
                    print("Je loopt door de volgende deur.")
                    print('')
                    time.sleep(1)
                    break


# === [kamer 3] === #

items = ("schild", "zwaard")

print('Je duwt het open en stap een hele lange kamer binnen.')
print(f'In deze kamer staat een tafel met daarbij een goblin.')
print(f"Op de tafel staan wat items. Dit zie je staan: {items}")
print(f"De goblin vraagt per item 1 rupee. Je kunt maar 1 van de ", (len(items)), " kiezen.")
item_keuze = input("Wil je het schild of het zwaard kopen? of niks? ")
if item_keuze == "schild":
    item = "schild"
    player_defense += 1
    print(f"Top je hebt voor het {item} gekozen.")
elif item_keuze == "zwaard":
    item = "zwaard"
    player_attack += 2
    print(f"Top je hebt voor het {item} gekozen.")
else:
    print("Je kiest ervoor om niks te kopen")

print('Op naar de volgende deur.')
print('')
time.sleep(1)


# === [kamer 4] === #

cpu_attack = 2
cpu_defense = 0
cpu_health = 3
cpu_hit_damage = (cpu_attack - player_defense)
player_hit_damage = (player_attack - cpu_defense)
if item_keuze == "schild" or item_keuze == "zwaard":
    print(f'Dapper met je nieuwe {item} loop je de kamer binnen.')
else:
    print("Je loopt de volgende kamer in")
print('Je loopt tegen een Cpu aan.')
print('')
time.sleep(1)

if cpu_hit_damage <= 0:
    print("Je hebt een te goede verdediging voor de Cpu, hij kan je geen schade toebrengen")
else:
    while cpu_health > 0 or player_health > 0:
            cpu_health -= player_hit_damage
            print(cpu_health, "Cpu")
            if cpu_health > 0:
                player_health -= cpu_hit_damage
                print(player_health, "Speler")
                if player_health > 0:
                    continue
                else:
                    print("Helaas je bent te gewond om verder door te gaan.")
                    print("Game Over")
                    exit()
                    # break
            else:
                print("Je hebt de Cpu gedood. ")
                print(f'Je health is nu {player_health}.')
                break

print('')
time.sleep(1)


# === [kamer 5] === #

print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
print("Er zit een slot op.")
print("Heb je de sleutel?") # kan veranderd worden
print('')
time.sleep(1)

if got_key == True:
    print("Gefeliciteerd, je hebt de schatkist geopend.")
    print("De gouden munten, kristallen en sieraden zijn van jou.")
else:
    print("Je hebt geen sleutel.")
    print("Game over")