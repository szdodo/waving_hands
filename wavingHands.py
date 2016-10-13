import os
import time

fLeft=""
fRight=""
sLeft=""
sRight=""
#damage taken
fDmg=0
sDmg=0
fShield=False
sShield=False
fCounter=False
sCounter=False

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
def hand_reading_first(): 
    global fLeft
    firstL=input("1. balkéz: ")
    fLeft=str(fLeft)+str(input_check(firstL))
    #print(fLeft)
    fLeft=spell_check(fLeft,1)

    global fRight
    firstR=input("1. jobbkéz: ")
    fRight=fRight+input_check(firstR)
    #print(fRight)
    fRight=spell_check(fRight,1)
    

def hand_reading_second(): 
    global sLeft
    secondL=input("2. balkéz: ")
    sLeft=sLeft+input_check(secondL)
    #print(sLeft)
    sLeft=spell_check(sLeft,2)

    global sRight
    secondR=input("2. jobbkéz: ")
    sRight=sRight+input_check(secondR)
    #print(sRight)
    sRight=spell_check(sRight,2)

def game_over():
    if fDmg>15:
        print("\n1. játékos ",fDmg," sebzést kapott!\nJáték vége!\nA második játékos nyert!\n")
    else:
        print("\n2. játékos ",sDmg," sebzést kapott!\nJáték vége!\nAz első játékos nyert!\n")
    quit()

def rounds(fL,fR,sL,sR):
    global fDmg
    global sDmg
    global fShield
    global sShield
    global fCounter
    global sCounter

    os.system('clear')

    if sDmg<15 and fDmg<15:
        print("\n1. JÁTÉKOS ",fDmg," SEBZÉST KAPOTT\nBal: ",fLeft,"\nJobb: ",fRight,"\n")
        fShield=False
        fCounter=False
        hand_reading_first()
    else:
        game_over()
    
    #2db if kell h nem menjen túl az életükön ha az egyik meghalna mér akkorse
    if fDmg<15 and sDmg<15:
        print("\n2. JÁTÉKOS ",sDmg," SEBZÉST KAPOTT\nBal: ",sLeft,"\nJobb: ",sRight,"\n")
        sShield=False
        sCounter=False
        hand_reading_second()
    else:
        game_over()
    time.sleep(0.5)
    rounds(fL,fR,sL,sR)


def counter_spell(num):
    global fCounter
    global sCounter
    
    if num==1:
        fCounter=True
        #print(fCounter)
    else:
        sCounter=True
        #print(sCounter)
    print('\033[92m' + '\033[1m' + "Counter-spell" + '\033[0m')

def shield(num):
    global fShield
    global sShield

    if num==1:
        fShield=True
        #print(fShield)
    else:
        sShield=True
        #print(sShield)
    print('\033[94m' + '\033[1m' + "Shield" + '\033[0m')

def missile(num):
    global fDmg
    global sDmg
    if num==1 and sShield==False and sCounter==False:
        sDmg=sDmg+1
    elif sCounter==True:
        fDmg=fDmg+1
    if num==2 and fShield==False and fCounter==False:
        fDmg=fDmg+1
    elif fCounter==True:
        sDmg=sDmg+1
    print('\033[95m' + '\033[1m' + "Missile" + '\033[0m')

def lightning_bolt(num):
    global fDmg
    global sDmg
    if num==1 and sCounter==False:
        sDmg=sDmg+5
    elif sCounter==True:
        fDmg=fDmg+5
    if num==2 and fCounter==False:
        fDmg=fDmg+5
    elif fCounter==True:
        sDmg=sDmg+5
    print('\033[93m' + '\033[1m' + "Lightning Bolt" + '\033[0m')

def cause_light_wounds(num):
    global fDmg
    global sDmg
    if num==1 and sCounter==False:
        sDmg=sDmg+2
    elif sCounter==True:
        fDmg=fDmg+2
    if num==2 and fCounter==False:
        fDmg=fDmg+2
    elif fCounter==True:
        sDmg=sDmg+2
    print('\033[91m' + '\033[1m' + "Cause Light Wounds" + '\033[0m')

def cause_heavy_wounds(num):
    global fDmg
    global sDmg
    if num==1 and sCounter==False:
        sDmg=sDmg+3
    elif sCounter==True:
        fDmg=fDmg+3
    if num==2 and fCounter==False:
        fDmg=fDmg+3
    elif fCounter==True:
        sDmg=sDmg+3
    print('\033[91m' + '\033[1m' + "Cause Heavy Wounds" + '\033[0m')

#stabet minden levédi
def stab(num):
    global fDmg
    global sDmg
    if num==1 and sShield==False:
        sDmg=sDmg+1
    if num==2 and fShield==False:
        fDmg=fDmg+1
    print('\033[91m' + '\033[1m' + "Stab" + '\033[0m')


gestures= {0:"WPP",1:"WWS",2:"PS",3:"SD",4:"DFFDD",5:"WDD",6:"WFP",7:"WPFD",8:">"}

spells={ "WPP" : counter_spell,
         "WWS": counter_spell,
         "SD": missile, 
         "DFFDD": lightning_bolt, 
         "WDD": lightning_bolt,
         "WFP": cause_light_wounds, 
         "WPFD": cause_heavy_wounds,
         "PS": shield,
         ">": stab}

def rules():
    os.system('clear')
    print('\033[1m' + "\nWAVING HANDS\n" + '\033[0m')
    print('\033[4m' +"Varázslatok:" + '\033[0m')
    print("WPP/WWS - Counter-spell\nSD - Missile\nDFFDD/WDD - Lightning Bolt")
    print("WFP - Cause Light Wounds\nWPFD - Cause Heavy Wounds\nPS - Shield\n> - Stab")
    ind = input("\nÍrj be valamit a kezdéshez!")
    if ind != "":
        rounds(fLeft,fRight,sLeft,sRight)



os.system('clear')
new_game=input("\n1 - Súgó\n2 - Új játék\n")

if new_game == '2':
    rounds(fLeft,fRight,sLeft,sRight)
elif new_game == '1':
    rules()
else:
    quit()
   
    
