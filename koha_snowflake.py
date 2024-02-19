import matplotlib.pyplot as plt
import matplotlib.patches as patches
import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)
 
            
def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()
    
    
    for _ in range(6):
        koch_curve(t, order, size)
        t.left(60)

    
 
    window.mainloop()
    
size = int(input('Enter size of recursion:'))
# Виклик функції
draw_koch_curve(3,size)
  
