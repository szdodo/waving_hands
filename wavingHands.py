fLeft=""
fRight=""
sLeft=""
sRight=""
fDamage=0
sDamage=0

spells={ "WPP" : "Counter-spell",
         "WWS": "Counter-spell",
         "P": "Shield", "SD": "Missile", 
         "DFFDD": "Lightning Bolt", 
         "WDDC": "Lightning Bolt",
         "WFP": "Cause Light Wounds", 
         "WPFD": "Cause Heavy Wounds",
         ">": "Stab"}



def input_check(letter):
    while letter!='W' and letter!='F' and letter!='P' and letter!='S' and letter!='D' and letter!='>' and letter !='':
        letter=input("Adja meg még egyszer! Csak 'W','F','P','S','D','>' vagy üres lehet!\n")
    return letter

def spells_check(hand):
    for each in spells:
        if hand == spells[each]:
            print("jó")
        else:
            print("nem jó")


def hand_reading(fLeft,fRight,sLeft,sRight):
    firstL=input("1. játékos bal kéz: ")
    fLeft=fLeft+input_check(firstL)

    firstR=input("1. játékos jobbkéz: ")
    fRight=fRight+input_check(firstR)

    secondL=input("2. játkos bal kéz: ")
    sLeft=sLeft+input_check(secondL)

    secondR=input("2. játékos jobbkéz: ")
    sRight=sRight+input_check(secondR)


hand_reading(fLeft,fRight,sLeft,sRight)
#spells_check(fLeft)

