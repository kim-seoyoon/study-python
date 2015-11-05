# sample timer program
# screen saver
import simplegui
import random

# global
message="Python is Fun!"
position = [50,50]
width=500
height=500
interval=2000

#handler for text box
def update(text):
    global message
    message=text

#handler for timer
def tick():
    x=random.randrange(0,width)
    y=random.randrange(0,height)
    position[0]=x
    position[1]=y


#handler
def draw(canvas):
    canvas.draw_text(message,position,36,"Red")

#create frame
frame=simplegui_create_frame("Home",widhth,height)

#register event
text=frame.add_input("Message",update,150)
frame.set_draw_handler(draw)
timer=simplegui.create_timer(interval,tick)

#start the frame
frame.start()
timer.start()
