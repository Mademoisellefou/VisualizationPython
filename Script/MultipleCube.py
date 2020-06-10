import turtle
my_turtle=turtle.Turtle()
my_win=turtle.Screen()
def draw_spiral(my_turtle,line_len):
    if line_len<200:
        my_turtle.forward(line_len)
        my_turtle.left(90)
        draw_spiral(my_turtle,line_len+20)
draw_spiral(my_turtle,0)
my_win.exitonclick()
    
