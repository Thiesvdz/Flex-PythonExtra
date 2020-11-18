import turtle

colors = ["red","blue","green","black","yellow"]
turtle.speed(175)
my_pen = turtle.Pen()
turtle.bgcolor("White")


for x in range(800):
    my_pen.pencolor(colors[x % 5])
    my_pen.forward(x)
    my_pen.right(125)
    
turtle.done()
