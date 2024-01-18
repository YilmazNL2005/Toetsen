import time, math
from random import randint
import random

player_attack = 1
player_defense = 0
player_health = 3

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

# === [kamer 2] === #
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

print('Je zie een deur achter het standbeeld.')
print('')
time.sleep(1)

# Kamer 6
# De zombie, die eerst in kamer 4 zat is hier naartoe verhuist. 
# Deze kamer zit tussen kamer 2 en 3.
# Tip: onderzoek of je de code voor gevechten herbruikbaar kan maken. 

zombie_attack = 1
zombie_defense = 0
zombie_health = 2
zombie_hit_damage = (zombie_attack - player_defense)

if zombie_hit_damage <= 0:
    print('Jij hebt een te goede verdediging voor de zombie, hij kan je geen schade toebrengen.')
else:
    zombie_hit_damage = (zombie_attack - player_defense)
    zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
    
    player_hit_damage = (player_attack - zombie_defense)
    player_attack_amount = math.ceil(zombie_health / player_hit_damage)
    
    zombie_attack_hits = zombie_attack_amount * zombie_attack
    player_health = player_health - zombie_attack_hits 
    if player_attack_amount < zombie_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de zombie te sterk voor je.')
        print('Game over.')
        exit()

# === [kamer 3] === #
items = ("schild", "zwaard")
welk_item = random.choice(items)
if welk_item == "schild":
    item = 'schild'
    player_defense += 1
else:
    item = "zwaard"
    player_attack += 2

print('Je duwt het open en stap een hele lange kamer binnen.')
print(f'In deze kamer staat een tafel met daarop een {item}.')
print(f'Je pakt het {item} op en houd het bij je.')
print('Op naar de volgende deur.')
print('')
time.sleep(1)

# === [kamer 4] === #

# In deze kamer zit een nieuwe vijand, deze vijand is sterker dan de zombie. 
# Hij heeft een attack van 2, een defence van 0 en een health van 3. 
# Ook hiermee vindt een gevecht plaats.
cpu_attack = 2
cpu_defense = 0
cpu_health = 3
cpu_hit_damage = (cpu_attack - player_defense)


print(f'Dapper met je nieuwe {item} loop je de kamer binnen.')
print('Je loopt tegen een Cpu aan.')




if cpu_hit_damage <= 0:
    print("Je hebt een te goede verdediging voor de Cpu, hij kan je geen schade toebrengen")
else:
    cpu_hit_damage = (cpu_attack - player_defense)
    cpu_attack_amount = math.ceil(player_health / cpu_hit_damage)

    player_hit_damage = (player_attack - cpu_defense)
    player_attack_amount = math.ceil(cpu_health / player_hit_damage)

    cpu_attack_hits = cpu_attack_amount * cpu_attack
    player_health = player_health - cpu_attack_hits
    if player_attack_amount < cpu_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de Cpu.')
        print(f'Je health is nu {player_health}.')
    else:
        print("Helaas de Cpu is te sterk voor je.")
        print("Game Over")
        exit()

print('')
time.sleep(1)

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
print("Er zit een slot op.")
print("Heb je de sleutel?")

if got_key == True:
    print("Gefeliciteerd, je hebt de schatkist geopend.")
    print("De gouden munten, kristallen en sieraden zijn van jou.")
else:
    print("Je hebt geen sleutel.")
    print("Game over")


