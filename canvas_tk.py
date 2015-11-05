from Tkinter import *
import time
#delay=time.sleep(1)

master = Tk()

def end_game():
    w.quit()
    
def game():
    global out,s
    out = s

def create_circle(x,y,r,wd):
    global w
    x1=x-r-wd/2
    y1=y-r-wd/2
    x2=x+r+wd/2
    y2=y+r+wd/2
    x3=x-r+wd/2
    y3=y-r+wd/2
    x4=x+r-wd/2
    y4=y+r-wd/2
    w.create_oval(x1,y1,x2,y2,fill="blue")
    w.create_oval(x3,y3,x4,y4,fill="white")
    

w = Canvas(master, width=300, height=300)
w.pack()

o1=create_circle(90,200,20,10)
o2=create_circle(210,200,20,10)

l1=w.create_line(50, 180, 250, 180,width='40',fill="red")
l2=w.create_line(55, 170, 90, 120,width='5',fill="red")
l3=w.create_line(90, 120, 130, 120,width='5',fill="red")
l4=w.create_line(180, 108, 180, 160,width='140',fill="red")

q = Button(master, text="quit", width=10, command=end_game)
q.pack()
'''
l2=w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
r1=w.create_rectangle(50, 25, 150, 75, fill="blue")
o1=w.create_oval(50, 125, 150, 175, fill="blue")

g = Button(master, text="go", width=10, command=game)
g.pack()

v = StringVar()
e = Entry(master, textvariable=v)
e.config(width='20')
e.pack()
v.set("100")
s = v.get()
out="test"
w = Message(master, text=out)
w.pack()
'''


mainloop()
'''



Note that items added to the canvas are kept until you remove them.
If you want to change the drawing, you can either use methods like coords,
itemconfig, and move to modify the items, or use delete to remove them.

canvas items
  create_arc(bbox,**options)
  create_bitmap(position,**options)
  create_image(position,**options)
  create_line(coords,**options)
  create_oval(bbox,**options)
  create_polygon(coords,**options)
  create_rectangle(bbox,**options)
  create_text(position,**options)
  create_window(position,**options)

change items
  w.coords(l1, 200,100,400,200) # change coordinates
  w.itemconfig(l2, fill="blue") # change color
  w.delete(l1) # remove

Checkbutton
  self.var = StringVar()
  c = Checkbutton(
        master, text="Color image", variable=self.var,
        onvalue="RGB", offvalue="L", command=a
        )
  c.pack()

Entry
  v = StringVar()
  e = Entry(master, textvariable=v)
  e.config(width='20')
  e.pack()
  v.set("a default value")
  s = v.get()

OptionMenu
  w = OptionMenu(master, variable, "one", "two", "three")
  w.pack()
  
2 Paned widget
  m = PanedWindow(orient=VERTICAL)
  m.pack(fill=BOTH, expand=1)
  top = Label(m, text="top pane")
  m.add(top)
  bottom = Label(m, text="bottom pane")
  m.add(bottom)

Top level widget
  top = Toplevel()
  top.title("About this application...")
  msg = Message(top, text=about_message)
  msg.pack()
  button = Button(top, text="Dismiss", command=top.destroy)
  button.pack()



button = Button(text, text="Click", command=click)
text.window_create(INSERT, window=button)
'''
