fLeft=""
fRight=""
sLeft=""
sRight=""
#damage taken
fDmg=0
sDmg=0
fProtection=False
sProtection=False

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
def hand_reading(): 
    global fLeft
    firstL=input("1. játékos bal kéz: ")
    fLeft=str(fLeft)+str(input_check(firstL))
    print(fLeft)

    global fRight
    firstR=input("1. játékos jobbkéz: ")
    fRight=fRight+input_check(firstR)
    print(fRight)

    global sLeft
    secondL=input("2. játkos bal kéz: ")
    sLeft=sLeft+input_check(secondL)
    print(sLeft)

    global sRight
    secondR=input("2. játékos jobbkéz: ")
    sRight=sRight+input_check(secondR)
    print(sRight)

    fLeft=spell_check(fLeft,1)
    fRight=spell_check(fRight,1)
    sLeft=spell_check(sLeft,2)
    sRight=spell_check(sRight,2)

def game_over():
    if fDmg==15:
        print("\nJáték vége!\nA második játékos nyert!\n")
    else:
        print("\nJáték vége!\nAz első játékos nyert!\n")

def rounds(fL,fR,sL,sR):
    global fDmg
    global sDmg
    global fProtection
    global sProtection
    if fDmg<15 and sDmg<15:
        print("\n",1,". kör\n")
        fProtection=False
        sProtection=False
        hand_reading()
        #fDmg+=2
        print(fDmg)
        print(sDmg)
        print(fProtection,sProtection)
        rounds(fL,fR,sL,sR)
    else:
        game_over()


def counter_spell(num):
    global fProtection
    global sProtection
    
    if num==1:
        fProtection=True
        print(fProtection)
    else:
        sProtection=True
        print(sProtection)
    print("Counter-spell")

def shield(num):
    global fProtection
    global sProtection

    if num==1:
        fProtection=True
        print(fProtection)
    else:
        sProtection=True
        print(sProtection)
    print("Shield")

def missile(num):
    global fDmg
    global sDmg
    if num==1 and sProtection==False:
        sDmg=sDmg+1
    if num==2 and fProtection==False:
        fDmg=fDmg+1
    
    print("Missile")

def lightning_bolt(num):
    global fDmg
    global sDmg
    if num==1 and sProtection==False:
        sDmg=sDmg+5
    if num==2 and fProtection==False:
        fDmg=fDmg+5
    print("Lightning Bolt")

def cause_light_wounds(num):
    global fDmg
    global sDmg
    if num==1 and sProtection==False:
        sDmg=sDmg+2
    if num==2 and fProtection==False:
        fDmg=fDmg+2
    print("Cause Light Wounds")

def cause_heavy_wounds(num):
    global fDmg
    global sDmg
    if num==1 and sProtection==False:
        sDmg=sDmg+3
    if num==2 and fProtection==False:
        fDmg=fDmg+3
    print("Cause Heavy Wounds")

#stabet minden levédi
def stab(num):
    global fDmg
    global sDmg
    if num==1 and sProtection==False:
        sDmg=sDmg+1
    if num==2 and fProtection==False:
        fDmg=fDmg+1
    print("Stab")


gestures= {0:"WPP",1:"WWS",2:"PS",3:"SD",4:"DFFDD",5:"WDD",6:"WFP",7:"WPFD",8:">"}

#WDDC-lightning bolt, nincs clap mert ahhoz 2 kéz kell
spells={ "WPP" : counter_spell,
         "WWS": counter_spell,
         "SD": missile, 
         "DFFDD": lightning_bolt, 
         "WDD": lightning_bolt,
         "WFP": cause_light_wounds, 
         "WPFD": cause_heavy_wounds,
         "PS": shield,
         ">": stab}

rounds(fLeft,fRight,sLeft,sRight)
#spell=spell_check("WPFSSDWPP")
#lines=["PL","WPFD","SD","WPP"]
#for line in lines:
#    func=spells[line]
#    func()
#alma="WSSWWS"
#print(alma.find("WSW"))
