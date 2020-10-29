import turtle

turtle.speed(25)
turtle.bgcolor("Black")
turtle.pencolor("Red")
#colors("white", "red", "orange", "blue")
#turtle.pencolor(colors[x % 4])


for x in range(720):
    turtle.forward(x)
    turtle.right(250)
    
turtle.done()
