import os
import time

fLeft = ""
fRight = ""
sLeft = ""
sRight = ""


class wizard:
    shield = False
    counter = False
    goblin = False
    troll = False
    halfLife = False
    damage = 0
    heatR = False
    coldR = False
    fire = False
    ice = False


fPlayer = wizard()
sPlayer = wizard()


def input_check(letter):
    while letter != 'W' and letter != 'F' and letter != 'P' and letter != 'S' and letter != 'D' and letter != '>' and letter != '':
        letter = input("Adja meg még egyszer! Csak 'W','F','P','S','D','>' vagy üres lehet!\n")
    return letter

# num=1 ha az első játékos, 2 ha a második játékos hívta meg


def spell_check(hand, num):
    for each in gestures:
        if hand.find(gestures[each]) != (-1):
            # print("jó")
            func = spells[gestures[each]]
            func(num)
            hand = ""
    return hand


# firtsL.. - beolvasáshoz kell, fLeft amit használunk
def hand_reading_first():
    global fLeft
    firstL = input("1. balkéz: ")
    fLeft = str(fLeft) + str(input_check(firstL))
    # print(fLeft)
    fLeft = spell_check(fLeft, 1)

    global fRight
    firstR = input("1. jobbkéz: ")
    fRight = fRight + input_check(firstR)
    # print(fRight)
    fRight = spell_check(fRight, 1)


def hand_reading_second():
    global sLeft
    secondL = input("2. balkéz: ")
    sLeft = sLeft + input_check(secondL)
    # print(sLeft)
    sLeft = spell_check(sLeft, 2)

    global sRight
    secondR = input("2. jobbkéz: ")
    sRight = sRight + input_check(secondR)
    # print(sRight)
    sRight = spell_check(sRight, 2)


#Itt csak kiírja, hogy ki a nyertes, a rounds()-ban ellenőriz


def game_over():
    if fPlayer.damage > 15:
        print("\n1. játékos ", fPlayer.damage, " sebzést kapott!\nJáték vége!\nA második játékos nyert!\n")
    else:
        print("\n2. játékos ", sPlayer.damage, " sebzést kapott!\nJáték vége!\nAz első játékos nyert!\n")
    quit()


def rounds():
    os.system('clear')

    if sPlayer.damage < 15 and fPlayer.damage < 15:
        print("\n1. JÁTÉKOS ", fPlayer.damage, " SEBZÉST KAPOTT\nBal: ", fLeft, "\nJobb: ", fRight, "\n")

        fPlayer.shield = False
        fPlayer.counter = False
        fPlayer.fire = False
        fPlayer.ice = False
        hand_reading_first()
        if fPlayer.goblin == True:
            sPlayer.damage = sPlayer.damage + 1
            print("Goblin")
        if fPlayer.troll == True:
            sPlayer.damage = sPlayer.damage + 2
            print("Troll")
        if fPlayer.heatR==True:
            print("Resist Heat")
        if fPlayer.coldR==True:
            print("Resist Cold")
    else:
        game_over()

    # 2db if kell h nem menjen túl az életükön ha az egyik meghalna mér akkorse
    if fPlayer.damage < 15 and sPlayer.damage < 15:
        print("\n2. JÁTÉKOS ", sPlayer.damage, " SEBZÉST KAPOTT\nBal: ", sLeft, "\nJobb: ", sRight, "\n")

        sPlayer.shield = False
        sPlayer.counter = False
        sPlayer.fire = False
        sPlayer.cold = False
        hand_reading_second()
        if sPlayer.goblin == True:
            fPlayer.damage = fPlayer.damage + 1
            print("Goblin")
        if sPlayer.troll == True:
            fPlayer.damage = fPlayer.damage + 2
            print("Troll")
        if sPlayer.heatR==True:
            print("Resist Heat")
        if sPlayer.coldR==True:
            print("Resist Cold")
    else:
        game_over()
    time.sleep(0.5)
    rounds()


def counter_spell(num):
    if num == 1:
        fPlayer.counter = True
        # print(fCounter)
    else:
        sPlayer.counter = True
        # print(sCounter)
    print('\033[92m' + '\033[1m' + "Counter-spell" + '\033[0m')


def shield(num):
    if num == 1:
        fPlayer.shield = True
    else:
        sPlayer.shield = True
    print('\033[94m' + '\033[1m' + "Shield" + '\033[0m')


def missile(num):
    if num == 1 and sPlayer.shield == False and sPlayer.counter == False:
        if sPlayer.troll == True and sPlayer.halfLife == False:
            sPlayer.halfLife = True
        elif sPlayer.troll == True and sPlayer.halfLife == True:
            sPlayer.troll = False
            sPlayer.halfLife = False
        elif sPlayer.goblin == True:
            sPlayer.goblin = False
        else:
            sPlayer.damage = sPlayer.damage + 1
    elif sPlayer.counter:
        fPlayer.damage = fPlayer.damage + 1
    if num == 2 and fPlayer.shield == False and fPlayer.counter == False:
        if fPlayer.troll == True and fPlayer.halfLife == False:
            fPlayer.halfLife = True
        elif fPlayer.troll == True and fPlayer.halfLife == True:
            fPlayer.troll = False
            fPlayer.halfLife = False
        elif fPlayer.goblin == True:
            fPlayer.goblin = False
        else:
            fPlayer.damage = fPlayer.damage + 1
    elif fPlayer.counter:
        sPlayer.damage = sPlayer.damage + 1
    print('\033[95m' + '\033[1m' + "Missile" + '\033[0m')


def lightning_bolt(num):
    if num == 1 and sPlayer.counter == False:
        if sPlayer.troll == True:
            sPlayer.troll = False
            sPlayer.halfLife = False
        elif sPlayer.goblin == True:
            sPlayer.goblin = False
        else:
            sPlayer.damage = sPlayer.damage + 5
    elif sPlayer.counter:
        fPlayer.damage = fPlayer.damage + 5
    if num == 2 and fPlayer.counter == False:
        if fPlayer.troll == True:
            fPlayer.troll = False
            fPlayer.halfLife = False
        elif fPlayer.goblin == True:
            fPlayer.goblin = False
        else:
            fPlayer.damage = fPlayer.damage + 5
    elif fPlayer.counter:
        sPlayer.damage = sPlayer.damage + 5
    print('\033[93m' + '\033[1m' + "Lightning Bolt" + '\033[0m')


def cause_light_wounds(num):
    if num == 1 and sPlayer.counter == False:
        if sPlayer.troll == True:
            sPlayer.troll = False
            sPlayer.halfLife = False
        elif sPlayer.goblin == True:
            sPlayer.goblin = False
        else:
            sPlayer.damage = sPlayer.damage + 2
    elif sPlayer.counter:
        fPlayer.damage = fPlayer.damage + 2
    if num == 2 and fPlayer.counter == False:
        if fPlayer.troll == True:
            fPlayer.troll = False
            fPlayer.halfLife = False
        elif fPlayer.goblin == True:
            fPlayer.goblin = False
        else:
            fPlayer.damage = fPlayer.damage + 2
    elif fPlayer.counter:
        sPlayer.damage = sPlayer.damage + 2
    print('\033[91m' + '\033[1m' + "Cause Light Wounds" + '\033[0m')


def cause_heavy_wounds(num):
    if num == 1 and sPlayer.counter == False:
        if sPlayer.troll == True:
            sPlayer.troll = False
            sPlayer.halfLife = False
        elif sPlayer.goblin == True:
            sPlayer.goblin = False
        else:
            sPlayer.damage = sPlayer.damage + 3
    elif sPlayer.counter:
        fPlayer.damage = fPlayer.damage + 3
    if num == 2 and fPlayer.counter == False:
        if fPlayer.troll == True:
            fPlayer.troll = False
            fPlayer.halfLife = False
        elif fPlayer.goblin == True:
            fPlayer.goblin = False
        else:
            fPlayer.damage = fPlayer.damage + 3
    elif fPlayer.counter:
        sPlayer.damage = sPlayer.damage + 3
    print('\033[91m' + '\033[1m' + "Cause Heavy Wounds" + '\033[0m')

# stabet minden levédi


def stab(num):
    if num == 1 and sPlayer.shield == False:
        if sPlayer.troll == True and sPlayer.halfLife == False:
            sPlayer.halfLife = True
        elif sPlayer.troll == True and sPlayer.halfLife == True:
            sPlayer.troll = False
            sPlayer.halfLife = False
        elif sPlayer.goblin == True:
            sPlayer.goblin = False
        else:
            sPlayer.damage = sPlayer.damage + 1
    if num == 2 and fPlayer.shield == False:
        if fPlayer.troll == True and fPlayer.halfLife == False:
            fPlayer.halfLife = True
        elif fPlayer.troll == True and fPlayer.halfLife == True:
            fPlayer.troll = False
            fPlayer.halfLife = False
        elif fPlayer.goblin == True:
            fPlayer.goblin = False
        else:
            fPlayer.damage = fPlayer.damage + 1
    print('\033[91m' + '\033[1m' + "Stab" + '\033[0m')


def cure_light_wounds(num):
    if num == 1 and fPlayer.damage != 0:
        fPlayer.damage = fPlayer.damage - 1
    elif num == 2 and sPlayer.damage != 0:
        sPlayer.damage = sPlayer.damage - 1
    print("Cure Light Wounds")


def cure_heavy_wounds(num):
    if num == 1 and fPlayer.damage != 0:
        if fPlayer.damage == 1:
            fPlayer.damage = 0
        else:
            fPlayer.damage = fPlayer.damage - 2
    elif num == 2 and sPlayer.damage != 0:
        if sPlayer.damage == 1:
            sPlayer.damage = 0
        else:
            sPlayer.damage = sPlayer.damage - 2
    print("Cure Heavy Wounds")


def summon_goblin(num):
    if num == 1:
        fPlayer.goblin = True
    else:
        sPlayer.goblin = True
    print_goblin()
    print("Summon Goblin")    


def summon_troll(num):
    if num == 1:
        fPlayer.troll = True
    else:
        sPlayer.troll = True
    print_troll()
    print("Summon Troll")


def fireball(num):
    if num == 1:
        fPlayer.fire = True
    else:
        sPlayer.fire = True
    if num == 1 and sPlayer.heatR == False and sPlayer.ice == False:
        sPlayer.damage = sPlayer.damage + 5
    if num == 2 and fPlayer.heatR == False and fPlayer.ice == False:
        fPlayer.damage = fPlayer.damage + 5
    print("Fireball")


def fire_storm(num):
    if num == 1:
        fPlayer.fire = True
    else:
        sPlayer.fire = True
    if num == 1 and sPlayer.heatR == False and sPlayer.ice == False:
        sPlayer.damage = sPlayer.damage + 5
    if num == 2 and fPlayer.heatR == False and fPlayer.ice == False:
        fPlayer.damage = fPlayer.damage + 5
    print("Fire Storm")


def ice_storm(num):
    if num == 1:
        fPlayer.ice = True
    else:
        sPlayer.ice = True
    if num == 1 and sPlayer.coldR == False and sPlayer.fire == False:
        sPlayer.damage = sPlayer.damage + 5
    if num == 2 and fPlayer.coldR == False and fPlayer.fire == False:
        fPlayer.damage = fPlayer.damage + 5
    print("Ice Storm")


def resist_heat(num):
    if num == 1:
        fPlayer.heatR = True
    else:
        sPlayer.heatR = True
    print("Resist Heat")


def resist_cold(num):
    if num == 1:
        fPlayer.coldR = True
    else:
        sPlayer.coldR = True
    print("Resist Cold")


def remove_enchantment(num):
    if num == 1 and sPlayer.counter == False:
        sPlayer.coldR = False
        sPlayer.heatR = False
    if num == 2 and fPlayer.counter == False:
        fPlayer.coldR = False
        fPlayer.heatR = False
    print("Remove Enchantment")


def print_goblin():
    print("         ,      ,")
    print("        /(.----.)\ ")
    print("    |\  \/      \/  /|")
    print("    | \ / =.  .= \ / |")
    print("    \( \   o\/o   / )/")
    print("     \_, '-/  \-' ,_/")
    print("       /   \__/   \"")
    print("       \ \__/\__/ /")
    print("     ___\ \|--|/ /___")
    print("   /`    \      /    `'\'")
    print("  /       '----'       '\'")

def print_winner():
    print("               _________")
    print("              |#########|")
    print("              |#########|")
    print("              |#########|")
    print("              |#########|")
    print("              |#########|")
    print("            __|_________|__")
    print("              |     '_ ' '\'")
    print("              F     (.) (.)--.__")
    print("             /                  `.")
    print("            J                    |")
    print("            F       ._          .'")
    print("           J          `-.____.-'")
    print("           F           '\'")
    print("          J             '\'")
    print("          |              '\'---")
    print("          |  .  `.        '\'_E")
    print("          |   `.  `.       L")
    print(" ,,,      |     `.  `.     |")
    print("\VVV'     |       `.  `    |")
    print(" \W|      J         ```    F")
    print("  `.    .' \              /")
    print("    `--'    )    ____.-  '")
    print("           /    /   `.   `.  .-")
    print("          /   .'      `.   `' /")
    print("          `.  \         `.   /")
    print("            `._|          `-'    ")


def print_troll():
    print("""
       .         __      '        .       '       .
  *            _-~  ~-_      .         '      .
 .   .        /___  ___\  '             .             .
             / (O)  (o) \         *         ___    *  .
   __,-~-~-,/    -..-    \  .-~~-.   __..-~~   ~~-.._
.-~  `V~V~V'`\ -v----v-   \/     /.-~  //..  \   \.  `~-._
  //.     \.' `\..___..---/    /''    """)

gestures = {
    0: "WPP",
    1: "WWS",
    2: "PS",
    3: "SD",
    4: "DFFDD",
    5: "WDD",
    6: "WFP",
    7: "WPFD",
    8: ">",
    9: "DFW",
    10: "DFPW",
    11: "SFW",
    12: "PFFW",
    13: "FSSPD",
    14: "SWWF",
    15: "WSSF",
    16: "WWPF",
    17: "SSFP",
    18: "PDWP"}

spells = {"WPP": counter_spell,
          "WWS": counter_spell,
          "SD": missile,
          "DFFDD": lightning_bolt,
          "WDD": lightning_bolt,
          "WFP": cause_light_wounds,
          "WPFD": cause_heavy_wounds,
          "PS": shield,
          ">": stab,
          "DFW": cure_light_wounds,
          "DFPW": cure_heavy_wounds,
          "SFW": summon_goblin,
          "PFFW": summon_troll,
          "FSSPD": fireball,
          "SWWF": fire_storm,
          "WSSF": ice_storm,
          "WWPF": resist_heat,
          "SSFP": resist_cold,
          "PDWP": remove_enchantment}


def rules():
    os.system('clear')
    print('\033[1m' + "\nWAVING HANDS\n" + '\033[0m')
    print('\033[4m' + "Varázslatok:" + '\033[0m')
    print("WPP/WWS - Counter-spell\nSD - Missile\nDFFDD/WDD - Lightning Bolt")
    print("WFP - Cause Light Wounds\nWPFD - Cause Heavy Wounds\nPS - Shield\n> - Stab")
    print("DFW - Cure Light Wounds\nDFPW - Cure HeavyWounds\nSFW - Summon Goblin\nPSFW - Summon Troll")
    ind = input("\nÍrj be valamit a kezdéshez!")
    if ind != "":
        rounds(fLeft, fRight, sLeft, sRight)


def main():
    os.system('clear')
    new_game = input("\n1 - Súgó\n2 - Új játék\n")

    if new_game == '2':
       rounds()
    elif new_game == '1':
        rules()
    else:
        quit()


if __name__ == '__main__':
    main()
