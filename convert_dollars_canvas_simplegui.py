# interactive application to convert a float in dollars and cents

import simplegui
#define global value

value = 3.12

#define funciions
def convert_units(val,name):
    result=str(val)+" "+name
    if val >1:
        result=result+"s"
    return result


def convert(val):
    # split into xx dollars and yy cents
    dollars=int(val)
    cents=round(100*(val-dollars))

    #convert to strings
    dollars_string = convert_units(dollars,"dollar")
    cents_string = convert_units(cents,"cents")

    #return composite string
    if dollars == 0 and cents ==0:
        return "Broke!"
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string

    
#define handler
def draw(canvas):
    canvas.draw_text(convert(value),60,110],24,"White")
    canvas.draw_circle([100,100],2,2,"Blue")

def input_handler(text):
    global value
    value = float(text)

# create frame
frame=simplegui.create_frame("converter",300,200)


# register draw handler
frame.set_draw_handler(draw)
frame.input_handler("Enter value", input_handler,100)


#start frame
frame.start()
