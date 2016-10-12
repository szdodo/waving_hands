fLeft=""
fRight=""
sLeft=""
sRight=""
#damage taken
fDmg=0
sDmg=0



def input_check(letter):
    while letter!='W' and letter!='F' and letter!='P' and letter!='S' and letter!='D' and letter!='>' and letter !='':
        letter=input("Adja meg még egyszer! Csak 'W','F','P','S','D','>' vagy üres lehet!\n")
    return letter

def spells_check(hand):
    for each in gestures:
        if hand == gestures[each]:
            #print("jó")
            func=spells[hand]
            func()
        #else:
            #print("nem jó")


def hand_reading(fLeft,fRight,sLeft,sRight):
    firstL=input("1. játékos bal kéz: ")
    fLeft=fLeft+input_check(firstL)

    firstR=input("1. játékos jobbkéz: ")
    fRight=fRight+input_check(firstR)

    secondL=input("2. játkos bal kéz: ")
    sLeft=sLeft+input_check(secondL)

    secondR=input("2. játékos jobbkéz: ")
    sRight=sRight+input_check(secondR)

def game_over(fDmg):
    if fDmg==15:
        print("\nJáték vége!\nA második játékos nyert!\n")
    else:
        print("\nJáték vége!\nAz első játékos nyert!\n")

def rounds(fLeft,fRight,sLeft,sRight,fDmg,sDmg):
    i=1
    if fDmg!=15 and sDmg!=15:
        print("\n",i,". kör\n")
        hand_reading(fLeft,fRight,sLeft,sRight)
        fDmg=fDmg+3
        print(fDmg)
        rounds(fLeft,fRight,sLeft,sRight,fDmg,sDmg)
    else:
        game_over(fDmg)


def counter_spell():
    print("Counter-spell")

def shield():
    print("Shield")

def missile():
    print("Missile")

def lightning_bolt():
    print("Lightning Bolt")

def cause_light_wounds():
    print("Cause Light Wounds")

def cause_heavy_wounds():
    print("Cause Heavy Wounds")


gestures= {0:"WPP",1:"WWS",2:"P",3:"SD",4:"DFFDD",5:"WDDC",6:"WFP",7:"WPFD",8:">"}

spells={ "WPP" : counter_spell,
         "WWS": counter_spell,
         "P": shield, 
         "SD": missile, 
         "DFFDD": lightning_bolt, 
         "WDDC": lightning_bolt,
         "WFP": cause_light_wounds, 
         "WPFD": cause_heavy_wounds,
         ">": "Stab"}

rounds(fLeft,fRight,sLeft,sRight,fDmg,sDmg)
spells_check("SD")
#lines=["PL","WPFD","SD","WPP"]
#for line in lines:
#    func=spells[line]
#    func()

