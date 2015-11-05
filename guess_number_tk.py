# Guess the number
#
# selections by buttons
# input and output in the console

# initialize global variables
from Tkinter import *
import random
import math

### class
 

### define event handlers for control panel

def start_game():
    # start new game
    global num_range,secret_number
    secret_number=random.randint(0,num_range)
    get_input()   

def end_game():
    exit()

def query_game():
    q=canvas.create_text(200,200,width=100,text='Game Over',fill='purple')
    btnB = Button(tk, text='Start', width=20, command=start_game)
    btnB.pack()
    time.sleep(0.5)
    btnS = Button(tk, text='Stop', width=20, command=end_game)
    btnS.pack()

def range100():
    # button that changes range to range [0,100) and restarts
    global max_try, num_range
    max_try=7
    num_range=100

def range1000():
    # button that changes range to range [0,1000) and restarts
    global max_try, num_range
    max_try=10
    num_range=1000


def get_input():

    # main game logic goes here
    global max_try,secret_number,num_range
    print "New game. Range is from 0 to ",num_range
    print "Number of remaining guesses is ",max_try
    print
    guess_n=1
    while (guess_n<=max_try):
        '''
        line_input=tk.Frame(root)
        entry_a = tk.Entry(line_input,width="40")
        guess = int(entry_a.get())
        '''
        guess=int(raw_input("enter number in [1, %d ):"%num_range))
        print
        print "Guess was ",guess
        print "Number of remaining guesses is ",max_try-guess_n
        
        if (guess == secret_number):
            print "Correct! You win!"
            end_game()
        elif (guess < secret_number):
            print "Higher"
        elif (guess > secret_number):
            print "Lower"

        print
        guess_n = guess_n +1
        

    print " You fail"
    print
    guess_n=1
        



#source=Tkinter.StringVar()
#source_string=source.get()

    '''
    guess_input(tk,text='guess',command=get_input(guess).pack(side=BOTTOM)
    help_btn = Tkinter.Menubutton(menu_frame, text='Help', underline=0)
    help_btn.pack(side=Tkinter.LEFT, padx="2m")
    help_btn.menu = Tkinter.Menu(help_btn)
    help_btn.menu.add_command(label="How To", underline=0, command=HowTo)
    help_btn.menu.add_command(label="About", underline=0, command=About)
    help_btn['menu'] = help_btn.menu

    q_window = Tkinter.Toplevel(tk)
    q_window.title('Guess number?')
    Tkinter.Entry(q_window, width=30, textvariable=guess).pack()
    Tkinter.Button(q_window, text="Number",command=lambda: update_specs()).pack()
    guess = Tkinter.StringVar()
    '''            
    line_btn = tk.Frame(tk)

    #Tkinter.Entry(get_window,width=100,textvariable=source).pack()
    tk.pack()
    tk.update()
    
### Main routine

num_range=100
max_try=7
secret_number =1

tk=Tk()

g=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
g.pack()

btn100 = Button(tk,text='Range is [0,100)',command=range100)
btn100.pack()

btn1000 = Button(tk,text='Range is [0,1000)',command=range1000)
btn1000.pack()

start_game()

tk.mainloop()
