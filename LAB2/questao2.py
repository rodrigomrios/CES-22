import turtle # Tess becomes a traffic light.
turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")

wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()
tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")
# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.
# This variable holds the current state of the machine
state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0: # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
        wn.ontimer(advance_state_machine, 5000)
    elif state_num == 1: # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
        wn.ontimer(advance_state_machine, 8000)
    else: # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0
        wn.ontimer(advance_state_machine, 5000)

def color_turn_red():
    tess.fillcolor("red")

def color_turn_green():
    tess.fillcolor("green")

def color_turn_blue():
    tess.fillcolor("blue")

shape_size = 3

def shape_size_up():
    global shape_size
    if shape_size >= 2 and shape_size < 4:
        shape_size = shape_size + 1
        tess.shapesize(shape_size)

def shape_size_down():
    global shape_size
    if shape_size > 2 and shape_size <= 4:
        shape_size = shape_size - 1  
        tess.shapesize(shape_size)   

pen_size = 3

def size_pen_up():
    global pen_size
    if pen_size >= 1 and pen_size < 20:
        pen_size = pen_size + 1
        tess.pensize(pen_size)

def size_pen_down():
    global pen_size
    if pen_size > 1 and pen_size <= 20:
        pen_size = pen_size - 1  
        tess.pensize(pen_size)   

def tess_turn_square():
    tess.shape("square")

def tess_turn_circle():
    tess.shape("circle")

def moves(a, b):
    tess.goto(a,b)

# Bind the event handler to the space key.

wn.ontimer(advance_state_machine, 5000)
wn.onkey(color_turn_red, "r")
wn.onkey(color_turn_blue, "b")
wn.onkey(color_turn_green, "g")
wn.onkey(shape_size_up, "Up")
wn.onkey(shape_size_down, "Down")
wn.onkey(size_pen_down, "-")
wn.onkey(size_pen_up, "+")
wn.onkey(tess_turn_circle, "c")
wn.onkey(tess_turn_square, "s")
wn.onclick(moves)
wn.listen() # Listen for events
wn.mainloop()