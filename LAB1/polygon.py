import turtle

def draw_poly(t, n, sz):
    
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

window = turtle.Screen() #Set up the window and its attributes
window.bgcolor("lightgreen") # Define the window's color
window.title("Turtle draw a regular polygon")
point = turtle.Turtle() # Create point
draw_poly(point, 8, 50) # Call the function to draw the regular polygon
window.mainloop()