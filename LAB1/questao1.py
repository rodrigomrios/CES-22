import turtle

def draw_sequence(t):
      
      t.pencolor("#ff007f")
      
      for j in range(5):
            
            for i in range(4):
                  
                  t.forward(20*(j + 1))
                  t.left(90)
            
            t.penup()
            t.goto(-10*(j + 1), -10*(j + 1))
            t.pendown()


window = turtle.Screen() #Set up the window and its attributes
window.bgcolor("lightgreen") # Define the window's color
window.title("Turtle draw a squares")
point = turtle.Turtle() # Create point
draw_sequence(point) # Call the function to draw the regular polygon
window.mainloop()