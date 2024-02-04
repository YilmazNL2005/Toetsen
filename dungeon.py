import time, math
from random import randint
import random

player_attack = 1
player_defense = 0
player_health = 3
player_bank_rupee = 0

got_key = False
got_dolk = False

eerste_getal = randint(10, 25)
tweede_getal = randint(-5, 75)
som = eerste_getal + tweede_getal

deurkeuze_kamer_2 = "Geen"
deurkeuze_kamer_3 = "Geen"
deurkeuze_kamer_4 = "Geen"
deurkeuze_kamer_6 = "Geen"
deurkeuze_kamer_7 = "Geen"
deurkeuze_kamer_8 = "Geen"
deurkeuze_kamer_9 = "Geen"


# === [kamer 1] === #

print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)


# === [kamer 7] === #

print("Je stapt door de deur en ziet een Rupee op de grond liggen.")
print("Wat je ermee kunt is nog een raadsel, je neemt het in ieder geval mee...")
time.sleep(1)
verdwijning_rupee = randint(1,10)
if verdwijning_rupee == 10:
    print("De rupee is plotseling verdwenen toen je het wilde oppakken")
else:
    player_bank_rupee += 1
    print(f"Je hebt {player_bank_rupee} rupee")    
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
    time.sleep(1)
    if antwoord == som:
        print('Het standbeeld laat een rupee vallen en je pakt het op')
        player_bank_rupee += 1
        print(f"Je hebt nu {player_bank_rupee} rupee.")
    else:
        print('Er gebeurt niets....')
    time.sleep(1)
    print('Je ziet een deur achter het standbeeld.')
    print("Maar links zie je ook een deur.")
    deurkeuze_kamer_2 = input("Welke van de twee deuren wil je nemen? (a) De deur achter het standbeeld of (Enter) de deur rechts van het standbeeld? ")
    print('')
    time.sleep(1)


# === [kamer 6] === #

# Wanneer de speler de zombie verslaat krijgt hij een dolk, 
# deze dolk geeft +1 op de attack waarde en kan in combinatie met het zwaard gebruikt worden.

    zombie_attack = 1
    zombie_defense = 0
    zombie_health = 2
    # entiteiten_lijst = [player_health, zombie_health]
    if deurkeuze_kamer_7 == "" or deurkeuze_kamer_2.lower() == "a":
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
                    print("De zombie heeft een dolk laten vallen. Deze kun je 1x gebruiken. Het geeft je 1+ attack damage")
                    got_dolk = True
                    print(f'Je health is nu {player_health}.')
                    print("Je loopt door de volgende deur.")
                    print('')
                    time.sleep(1)
                    break
        deurkeuze_kamer_6 = input("Je ziet 2 deuren. (Enter) Wil je rechtdoor gaan of (a) wil je naar rechts? ")
        time.sleep(1)


# === [kamer 8] === #

if deurkeuze_kamer_7 == "" or deurkeuze_kamer_2 == "" or deurkeuze_kamer_6 == "a":
    print("Je stapt in een hele lange kamer")
    print("Je ziet een gokmachine staan en loopt er naartoe.")
    gok_keuze = input("(a) Wil je de gokmachine gebruiken of (Enter) niet? ")
    dobbelsteen_1 = randint(1, 6)
    dobbelsteen_2 = randint(1, 6)
    got_dices = dobbelsteen_1 + dobbelsteen_2
    if gok_keuze == "a":
        print("De gokmachine gaat 2 dobbelstenen dobbelen. Bij 7 ogen krijg je iets, hoger krijg je iets, maar als het onder de 7 is. Krijg je -1 hp")
        time.sleep(1)
        print(f"De eerste dobbelsteen: {dobbelsteen_1}")
        time.sleep(1)
        print(f"De tweede dobbelsteen: {dobbelsteen_2}")
        time.sleep(1)
        print(f"Samen heb je {got_dices} ogen gegooid.")
        if got_dices < 7:
            player_health -= 1
            print("Helaas je hebt te weinig ogen.")
            print(f"Er gaat -1 health van je totaal af. Nu heb je nog {player_health} hp.")
            if player_health <= 0:
                print("Helaas je bent te gewond om verder door te gaan.")
                print("Game Over")
                exit()
        elif got_dices == 7:
            print("Je hebt precies 7 ogen. Je krijgt +1 rupee en +4 health")
            player_bank_rupee += 1
            player_health += 4
            print(f"Je hebt nu {player_bank_rupee} rupee en {player_health} health. ")
        else:
            print("Je hebt meer dan 7 ogen. Het aantal rupee en health dat je hebt is zojuist verdubbeld.")
            player_bank_rupee += player_bank_rupee
            print(f"Je hebt nu {player_bank_rupee} rupee. ")
    deurkeuze_kamer_8 = input("Je ziet 2 deuren. (Enter) Wil je links gaan of (a) wil je naar rechts? ")
    print('')
    time.sleep(1)


# === [kamer 9] === #

if deurkeuze_kamer_8 == "a":
        health_defense = randint(1,2)
        print("Je ziet dat de gehele kamer een vreemde glinstering heeft. Misschien is het betoverd")
        time.sleep(1)
        if health_defense == 1:
            print(f"Je krijgt +{health_defense} defense erbij.")
            player_defense += 1
            print(f"Je hebt nu {player_defense} defense.")
        else:
            print(f"Je krijgt +{health_defense} health erbij.")
            player_health += 2
            print(f"Je hebt nu {player_health} health.")
        deurkeuze_kamer_9 = input("Je ziet twee deuren. wil je naar (Enter) links of (a) rechtdoor? ")
        print("")
        time.sleep(1)


# === [kamer 3] === #

items_goblin = ["schild", "bom", "sleutel"]
items_player = []
item_keuze = None
if deurkeuze_kamer_9 == "" or deurkeuze_kamer_8 == "" or deurkeuze_kamer_6 == "":
    print('Je duwt de volgende deur open en stapt binnen in een grote kamer.') # grammatica goed checken. Verbeterd
    print(f'In deze kamer staat een tafel met daarbij een goblin.')
    print(f"Op de tafel staan wat items. Dit zie je staan: {items_goblin}")
    if player_bank_rupee <= 0:
        print("Je hebt geen rupees om te besteden.")
        time.sleep(1)
    while player_bank_rupee >= 1:
        print(f"Je hebt op dit moment {player_bank_rupee} rupees.")
        print(f"De goblin vraagt per item 1 rupee. Je kunt 1 van de ", (len(items_goblin)), " items kiezen.")
        item_keuze = input("Welk item wil je kopen? of (Enter) niks? ")
        if item_keuze == "schild" and item_keuze in items_goblin:
            item = "schild"
            player_defense += 1
            print(f"Top je hebt voor het {item} gekozen.")
            items_goblin.remove(item_keuze)
            items_player.append(item_keuze)
            print(f"Dit is je inventory: {items_player}")
            player_bank_rupee -= 1
        elif item_keuze == "bom" and item_keuze in items_goblin:
            item = "bom"
            player_attack += 2
            print(f"Top je hebt voor de {item} gekozen.")
            items_goblin.remove(item_keuze)
            items_player.append(item_keuze)
            print(f"Dit is je inventory: {items_player}")
            player_bank_rupee -= 1
        elif item_keuze == "sleutel" and item_keuze in items_goblin:
            item = "sleutel"
            got_key = True
            print(f"Top je hebt voor de {item} gekozen.")
            items_goblin.remove(item_keuze)
            items_player.append(item_keuze)
            print(f"Dit is je inventory: {items_player}")
            player_bank_rupee -= 1
        else:
            if item_keuze == "":
                print("Je kiest ervoor om niks te kopen")
                print(f"Inventory: {items_player}")
                break
            elif item_keuze not in items_goblin:
                print(f"{item_keuze} heeft de goblin niet.")
    print('Je ziet twee deuren.')
    deurkeuze_kamer_3 = input("Kies je (Enter) de linker deur of (a) de rechter deur? ")
    print('')
    time.sleep(1)


# === [kamer 11] === #

    if deurkeuze_kamer_3 != "a":
        print("Je loopt een grote kamer binnen.")
        time.sleep(2)
        print("Er vliegen pijlen uit de muur.")
        print("Gebruik je schild")
        time.sleep(2)
        if "schild" not in items_player:
            print("Je hebt geen schild. Je wordt geraakt door meerdere pijlen.")
            time.sleep(1)
            print("Helaas je bent te gewond om verder door te gaan.")
            print("Game over!")
            exit()
        if "schild" in items_player:
            print("Je rent door alle beschietingen heen naar de volgende deur.")
            time.sleep(1)
            print("Fijn, zo'n schild")
            print("")
            time.sleep(2)


# === [kamer 4] === #

cpu_attack = 2
cpu_defense = 0
cpu_health = 3
if deurkeuze_kamer_3 == "a" or deurkeuze_kamer_9 == "a":
    cpu_hit_damage = (cpu_attack - player_defense)
    player_hit_damage = (player_attack - cpu_defense)
    print(player_hit_damage)
    time.sleep(3)
    if got_dolk:
        player_hit_damage += 1
        print(player_hit_damage)
        time.sleep(3)
        got_dolk = False
    if item_keuze == "schild" or item_keuze == "zwaard":
        print(f'Dapper met je nieuwe {item} loop je de kamer binnen.') # Nu benoemd de print maar 1 item. Het laatste wat gekocht is. Een list met de gekochte items kan het evt oplossen.
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
        time.sleep(1)
        

        # === [kamer 13] === #

        print("Deze muur is beschadigd, maar kan niet gesloopt worden zonder bom.")
        if "bom" not in items_player:
            print("Helaas, je hebt geen bom dus je kunt niet achter de muur komen.")
            time.sleep(1)
        if "bom" in items_player:
            print("Met behulp van de bom, is het gelukt om de muur op te blazen.")
            print("Er ligt een zwaard en dat neem je mee.")
            time.sleep(1)
            player_attack += 2
            items_player.remove("bom")
            items_player.append("zwaard")
            print(f"Je inventory: {items_player}")
            time.sleep(1)
        deurkeuze_kamer_4 = input("Je ziet 2 deuren. Wil je (Enter) rechtdoor gaan of (a) de rechtse deur nemen? ")
        if deurkeuze_kamer_4 == "a":
            time.sleep(2)
            # === [kamer 12] === #
            print("Je opent de deur. Je valt in een diepe put. Hier kom je niet uit en je bent te gewond om verder door te gaan.")
            print("Game Over")
            exit()
    print('')
    time.sleep(1)


# === [kamer 10] === #

boss_attack = 3
boss_defense = 1
boss_health = 5
boss_hit_damage = (boss_attack - player_defense)
player_hit_damage = (player_attack - boss_defense)
print(player_hit_damage)
time.sleep(3)
if got_dolk:
    player_hit_damage += 1
    print(player_hit_damage)
    time.sleep(3)
    got_dolk = False                                        # Heeft weinig nut als dit het laatste gevecht van de Dungeon is. Scheelt weer een regel code.
print("Je komt een erg grote kamer binnen")
time.sleep(1)
print("Het is de Dungeon Boss")
print("Om langs de volgende deur te gaan, moet je de boss doden.")
time.sleep(1)
if player_hit_damage < 0:
    print("De Dungeon Boss is te sterk.")
    print("Game Over")
    exit()
else:
    while boss_health > 0 or player_health > 0:
        boss_health -= player_hit_damage
        print(boss_health, "Boss")
        if boss_health > 0:
            player_health -= boss_hit_damage
            print(player_health, "Speler")
            if player_health > 0:
                continue
            else:
                print("Helaas je bent te gewond om verder door te gaan.")
                print("Game Over")
                exit()
        else:
            print("Je hebt de Dungeon Boss gedood. ")
            print(f'Je health is nu {player_health}.')
            break
print("")
time.sleep(2)


# === [kamer 5] === #

print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
print("Er zit een slot op.")
print("Heb je de sleutel?") # kan veranderd worden
print('')
time.sleep(1)

if got_key == True or "bom" in items_player:
    print("Gefeliciteerd, je hebt de schatkist geopend.")
    print("De gouden munten, kristallen en sieraden zijn van jou.")
else:
    print("Je hebt geen sleutel of bom om te gebruiken.")
    print("Game over")