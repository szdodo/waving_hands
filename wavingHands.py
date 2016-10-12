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

#num=1 ha az első játékos, 2 ha a második játékos hívta meg
def spell_check(hand,num):
    for each in gestures:
        if hand.find(gestures[each]) != (-1):
            #print("jó")
            func=spells[gestures[each]]
            func(num)
            hand=""
    return hand
        

#firtsL.. - beolvasáshoz kell, fLeft amit használunk
def hand_reading(fL,fR,sL,sR): 
    global fLeft
    firstL=input("1. játékos bal kéz: ")
    fLeft=str(fLeft)+str(input_check(firstL))
    #print(fLeft)
    fLeft=spell_check(fLeft,1)
    print(fLeft)

    global fRight
    firstR=input("1. játékos jobbkéz: ")
    fRight=fRight+input_check(firstR)
    fRight=spell_check(fRight,1)
    print(fRight)

    global sLeft
    secondL=input("2. játkos bal kéz: ")
    sLeft=sLeft+input_check(secondL)
    sLeft=spell_check(sLeft,2)
    print(sLeft)

    global sRight
    secondR=input("2. játékos jobbkéz: ")
    sRight=sRight+input_check(secondR)
    sRight=spell_check(sRight,2)
    print(sRight)

def game_over(fDmg):
    if fDmg==15:
        print("\nJáték vége!\nA második játékos nyert!\n")
    else:
        print("\nJáték vége!\nAz első játékos nyert!\n")

def rounds(fL,fR,sL,sR,fDmg, sDmg):
    if fDmg!=15 and sDmg!=15:
        print("\n",1,". kör\n")
        hand_reading(fL,fR,sL,sR)
        fDmg+=3
        print(fDmg)
        rounds(fL,fR,sL,sR,fDmg,sDmg)
    else:
        game_over(fDmg)


def counter_spell(num):
    print("Counter-spell")

def shield(num):
    print("Shield")

def missile(num):
    print("Missile")

def lightning_bolt(num):
    print("Lightning Bolt")

def cause_light_wounds(num):
    print("Cause Light Wounds")

def cause_heavy_wounds(num):
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

rounds(fLeft,fRight,sLeft,sRight,fDmg, sDmg)
spell=spell_check("WPFSSDWPP")
#lines=["PL","WPFD","SD","WPP"]
#for line in lines:
#    func=spells[line]
#    func()
alma="WSSWWS"
#print(alma.find("WSW"))
