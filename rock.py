# Mini-Project
# Rock-paper-Scissors-Lizard-Spock
#
import random

def name_to_number(name):
    if(name=="rock"): return 0
    elif(name=="spock"): return 1
    elif(name=="paper"): return 2
    elif(name=="lizard"): return 3
    elif(name=="scissors"): return 4
    else: print "error: wrong selection"

def number_to_name(number):
    if(number==0): return "rock"
    elif(number==1): return "spock"
    elif(number==2): return "paper"
    elif(number==3): return "lizard"
    elif(number==4): return "scissors"
    else: print "error: wrong selection"

def rpsls(player_choice):
    player_number=name_to_number(player_choice)
    #comp_number=int(random.randrange(5))
    comp_number=random.randint(0,4)
    comp_choice=number_to_name(comp_number)
    print "Player chooses",player_choice
    print "Computer chooses",comp_choice

    fight=(comp_number-player_number)%5
    

    if (fight==0): result=0
    elif (fight<=2): result=-1
    elif (fight>2): result=1
    else: print

    if (result==0): print "tie"
    elif (result==1): print "Player wins!"
    elif (result==-1): print "Computer wins!"
    else: print "Wrong situation"

keyin="r"
while(keyin!="q"):
    keyin = raw_input('Enter [R]ock, [S]pock, [P]aper, [L]izard, s[C]issors, [Q]uit:')
    keyin=keyin.lower()
    #test="scissors"
    if (keyin=='r'):player_choice="rock"
    elif(keyin=='s'):player_choice="spock"
    elif(keyin=='p'):player_choice="paper"
    elif(keyin=='l'):player_choice="lizard"
    elif(keyin=='c'):player_choice="scissors"
    elif(keyin=='q'):quit()
    else:
        print "try other character"
        continue
    print ""
    rpsls(player_choice)
    print ""






    
        
