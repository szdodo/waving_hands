fLeft="WW"
fRight=""
sLeft=""
sRight=""
#damage taken
fDmg=0
sDmg=0
fSpell=""



def input_check(letter):
    while letter!='W' and letter!='F' and letter!='P' and letter!='S' and letter!='D' and letter!='>' and letter !='':
        letter=input("Adja meg még egyszer! Csak 'W','F','P','S','D','>' vagy üres lehet!\n")
    return letter

def spell_check(hand):
    for each in gestures:
        if hand.find(gestures[each]) != (-1):
            #print("jó")
            func=spells[gestures[each]]
            func()
            hand=""
            return hand
        #else:
            #return hand

#firtsL.. - beolvasáshoz kell, fLeft amit használunk
def hand_reading(fLeft,fRight,sLeft,sRight): 
    firstL=input("1. játékos bal kéz: ")
    fLeft=fLeft+input_check(firstL)
    print(fLeft)
    fLeft=spell_check(fLeft)
    print(fLeft)

    firstR=input("1. játékos jobbkéz: ")
    fRight=fRight+input_check(firstR)
    fRight=spell_check(fRight)

    secondL=input("2. játkos bal kéz: ")
    sLeft=sLeft+input_check(secondL)
    sLeft=spell_check(sLeft)

    secondR=input("2. játékos jobbkéz: ")
    sRight=sRight+input_check(secondR)
    sRight=spell_check(sRight)

def game_over(fDmg):
    if fDmg==15:
        print("\nJáték vége!\nA második játékos nyert!\n")
    else:
        print("\nJáték vége!\nAz első játékos nyert!\n")

def rounds(fLeft,fRight,sLeft,sRight,fDmg,sDmg):
    if fDmg!=15 and sDmg!=15:
        print("\n",1,". kör\n")
        hand_reading(fLeft,fRight,sLeft,sRight)
        fDmg+=3
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

#WDDC-lightning bolt, nincs clap mert ahhoz 2 kéz kell
spells={ "WPP" : counter_spell,
         "WWS": counter_spell,
         "P": shield, 
         "SD": missile, 
         "DFFDD": lightning_bolt, 
         "WDD": lightning_bolt,
         "WFP": cause_light_wounds, 
         "WPFD": cause_heavy_wounds,
         ">": "Stab"}

rounds(fLeft,fRight,sLeft,sRight,fDmg,sDmg)
spell=spell_check("WPFSSDWPP")
#lines=["PL","WPFD","SD","WPP"]
#for line in lines:
#    func=spells[line]
#    func()
alma="WSSWWS"
#print(alma.find("WSW"))
