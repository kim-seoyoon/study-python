# sample timer program
# stopwatch
from Tkinter import *
import time
import tkFont

# global

time=0
wtime=0
time0=0
score=0
run=0
reset_flag=0

#handler for text box
def time_out(time):
    # input is ABCD(integer) output format as A:BC.D (A=min)
    m=int(time/600)
    #s=int((time-m*600)/10)
    s=int((time%600)/10)
    ms=time-m*600-s*10
    return str(m)+":"+str(int(s/10))+str(s%10)+"."+str(ms)
    
  
def s():
    global run,time,time0
    run=1
    time0=time
       
def e():
    global run,score,wtime
    run=0
    if (wtime%10==0 and wtime!=0):
        score+=1
    
def r():
    global wtime,time,time0,score
    wtime=0
    time=0
    time0=1
    score=0
        
 
#handler for timer
       
def tick(label):
  def count():
    global time,wtime,time0,score,run,reset_flag
    time += 1
    if run==0: time0=time
    wtime+=(time-time0)
    if wtime<0: wtime=0
    
    watch=time_out(wtime)
    label.config(text=watch)
    status.config(text="score "+str(score))
    label.after(100, count)
  count()
    
#start the frame
tk=Tk()
tk.title('Stopwatch')
f=Frame(tk)
f.pack()
# another method to using StringVar
#watch=StringVar()
#watch.set("0:00.0")
watch='0:00.0'
label=Message(tk,text=watch,fg='Red')
label.pack()



status=Label(tk,text='stop',fg='Blue')
status.pack()

tick(label)

btnstart=Button(tk,text='Start',width=50,command=s)
btnstart.pack()
btnstop=Button(tk,text='Stop',width=50,command=e)
btnstop.pack()
btnreset=Button(tk,text='Reset score',width=50,command=r)
btnreset.pack()

tk.mainloop()


    
"""
Block for simplegui
#handler
def draw(canvas):
    canvas.draw_text(watch,[100,100],36,"Red")

#create frame
frame=simplegui_create_frame("Home",300,300)

#register event
btnstart=frame.add_button("Start",start,150)
btnstop=frame.add_button("Stop",stop,150)
frame.set_draw_handler(draw)
timer=simplegui.create_timer(100,tick)

#start the frame
frame.start()
timer.start()
"""
